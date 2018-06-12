import csv
from pymongo import MongoClient
import logging
import json
import unidecode


class AfiliadosUploader:

    def __init__(self):
        """clase que sube los resultados DB de Afiliados CCB"""
        with open('src/config/dbconfig.json', 'r') as f:
            config = json.load(f)
            dburl = config['DEV']['DBURL']
            dbport = int(config['DEV']['DBPORT'])
            self.client = MongoClient(dburl, dbport)

        self.labels = []

        self.db = self.client.phystech
        self.collection = self.db.ccbafiliados
        ### ... result = self.collection.delete_many({})
        logging.basicConfig(filename='logs/uploader.log',
                            level=logging.DEBUG,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%m-%d-%y %H:%M')

    def convertLabel(self, label):
        lower = label.lower().replace("/", "").replace(".", "").replace(" ", "_").replace("__", "_").replace("%", "pc")
        variable = unidecode.unidecode(lower)
        return variable

    def isfloat(self, x):
        try:
            a = float(x)
        except ValueError:
            return False
        else:
            return True

    def getCIIU(self, description):
        try:
            val = float(description.split()[0])
            return val
        except IndexError:
            return 0

    def uploarResultfromCSV(self, csvfile):

        batch_data = []
        counter = 0

        with open(csvfile, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, dialect="excel-tab")
            labels = next(reader)
            for label in labels:
                converted = self.convertLabel(label)
                self.labels.append(converted)
            print(self.labels)

            ciiu_pos = [i for i, x in enumerate(self.labels) if "ciiu" in x]
            print(ciiu_pos)

            for row in reader:
                i=0
                data = {}
                for item in row:
                    if item.isdigit():
                        data[self.labels[i]] = int(item)
                    elif self.isfloat(item):
                        data[self.labels[i]] = float(item)
                    elif i in ciiu_pos:
                        data[self.labels[i]] = self.getCIIU(item)
                    else:
                        data[ self.labels[i]] = item
                    i += 1

                obj_id = self.collection.insert_one(data)
                logging.info('Total data read \t' + str(obj_id) + '\t' + str(counter))
                counter += 1

        print(counter)


