from pymongo import MongoClient
import json
import csv

BILLION = 1000000000
TIPOLO = {"ESTRIC": 1, "AMPLIA": 2, "POTENC": 3, "NOINNO": 4, "INTENC": 5}


class Exporter:

    def __init__(self):
        """clase que sube los resultados encuesta DANE en nuestra DB"""
        with open('../config/dbconfig.json', 'r') as f:
            config = json.load(f)
            dburl = config['DEV']['DBURL']
            dbport = int(config['DEV']['DBPORT'])
            self.client = MongoClient(dburl, dbport)

        self.db = self.client.phystech
        self.collection = self.db.editresults

    def getProjections(self, paramlist):
        select = {key: 1 for key in paramlist}
        select["_id"] = 0
        return self.collection.find({}, select)

    def exportToCSV(self, variables):
        print("export to CSV")

        for key, value in TIPOLO.items():
            try:

                filename = 'selection_' + key + '.csv'
                path = "../data/export/" + filename

                with open(path, 'w', encoding='utf-8', newline='') as f:
                    writer = csv.writer(f, dialect="excel-tab")
                    cursor = self.getProjections(variables)
                    headers = cursor.next()
                    header = []
                    for hd in headers:
                        header.append(hd)

                    writer.writerow(header)

                    for data in cursor:
                        row=[]
                        tipolo = TIPOLO[data["TIPOLO"]]
                        for itr, val in data.items():
                            if itr == "I3R2C1":
                                row.append(val / BILLION)
                            elif itr == "I3R2C2":
                                row.append(val / BILLION)
                            else:
                                row.append(val)

                        if tipolo == value:
                            writer.writerow(row)
                f.close()

            except IOError:
                print("cannot write file")


variables = ["CIIU4", "I3R2C1", "I3R2C2", "TIPOLO", "IV1R11C2"]

for i in range(1,16):
    var = "I2R"+str(i)+"C1"
    variables.append(var)

variables.append("I1R4C1")
variables.append("I1R4C2")
variables.append("I1R5C1")
variables.append("I1R5C2")
variables.append("I1R6C1")
variables.append("I1R6C2")

print(variables)
expo = Exporter()
expo.exportToCSV(variables)



