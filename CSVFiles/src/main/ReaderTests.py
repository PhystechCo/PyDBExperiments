import csv
from pymongo import MongoClient


class ReaderTests:
    """Class for testing the diferent possibliites"""
    def __init__(self):
        self.data_path = './data/'
        self.data = []
        self.client = MongoClient('localhost:27017')
        self.db = self.client.tests
        self.collection = self.db.csvtests

    def openTxtFromExcel(self, txtfile):
        try:
            with open(self.data_path + txtfile, 'r', encoding='utf-8') as f:
                reader = csv.reader(f, dialect="excel-tab")
                for row in reader:
                    line = []
                    idx = 0
                    data = {}
                    for col in row:
                        line.append(str(col))
                        data['col'+str(idx)] = str(col)
                        idx += 1

                    self.data.append( data)

                    row_line = '\t'.join(line)
                    print(row_line)

        except IOError as ex:
            print(ex.errno)

    def saveTxtFromExcelToDB(self):
        try:
            for dt in self.data:
                self.collection.insert_one(dt)
        except Exception as ex:
            print(ex)
