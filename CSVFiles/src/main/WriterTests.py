import csv
from pymongo import MongoClient


class WriterTests:
    """Class for testing the diferent possibliites"""
    def __init__(self):
        self.data_path = './data/export/'
        self.data = []
        self.client = MongoClient('localhost:27017')
        self.db = self.client.tests
        self.collection = self.db.csvtests

    def exportDataToCSV(self, csvfile):
        try:
            path = self.data_path + csvfile
            with open(path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f, dialect="excel", delimiter=';')

                cursor = self.collection.find({}, {"_id": 0})
                header = cursor.next()
                writer.writerow(header)

                for content in cursor:
                    print(content)
                    rwo = []
                    for key in content:
                        rwo.append(str(content[key]))
                    writer.writerow(rwo)

            f.close()

        except IOError as ex:
            print("ERROR#: " + str(ex.errno))
            print(str(ex.strerror))

        except AttributeError as ex:
            print(str(ex))

