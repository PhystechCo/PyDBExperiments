import csv
from pymongo import MongoClient
import logging
import json


class ReseultsUploader:

    def __init__(self):
        """clase que sube los resultados encuesta DANE en nuestra DB"""
        with open('src/config/dbconfig.json', 'r') as f:
            config = json.load(f)
            dburl = config['DEV']['DBURL']
            dbport = int(config['DEV']['DBPORT'])
            self.client = MongoClient(dburl, dbport)

        self.labels = []

        self.db = self.client.phystech
        self.collection = self.db.editresults
        # ... result = self.collection.delete_many({})
        logging.basicConfig(filename='logs/uploader.log',
                            level=logging.DEBUG,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%m-%d-%y %H:%M')

    def uploarResultfromCSV(self, csvfile):

        batch_data = []
        counter = 0

        with open(csvfile, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f, delimiter=';')
            labels = next(reader)
            for label in labels:
                self.labels.append(label)
            for row in reader:
                i=0
                data = {}
                for item in row:
                    if i == 2:
                        data[self.labels[i]] = item
                    else:
                        if item == ' ':
                            data[ self.labels[i]] = 0
                        else:
                            data[ self.labels[i]] = int(item)
                    i += 1
                batch_data.append(data)
                counter += 1

        obj_id = self.collection.insert_many(batch_data)
        logging.info('Total data read \t' + str(obj_id) + '\t' + str(counter))
