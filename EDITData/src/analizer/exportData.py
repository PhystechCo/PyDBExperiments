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
        self.varcollection = self.db.editvariables

    def getProjections(self, paramlist):
        select = {key: 1 for key in paramlist}
        select["_id"] = 0
        return self.collection.find({}, select)

    def getProjectionsOne(self, paramlist):
        select = {key: 1 for key in paramlist}
        select["_id"] = 0
        return self.collection.find_one({}, select)

    def exportToCSV(self, variables):
        print("export to CSV")

        for key, value in TIPOLO.items():
            try:

                filename = 'selection_' + key + '.csv'
                path = "../data/export/" + filename

                n_column = 0
                column_indexes = []

                with open(path, 'w', encoding='utf-8', newline='') as f:
                    writer = csv.writer(f, dialect="excel-tab")
                    headers = self.getProjectionsOne(variables)

                    print(headers)
                    header = []
                    for hd in headers:
                        header.append(hd)
                        column_indexes.append([hd, n_column])
                        n_column += 1

                    writer.writerow(header)

                    cursor = self.getProjections(variables)

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

                for col_ind in column_indexes:
                    info = str(col_ind[0]) + '\t' + str(col_ind[1])
                    print(info)

            except IOError:
                print("cannot write file")

    def getVarLabels(self, variables):
        for var in variables:
            select = {"_id": 0, "Etiqueta": 1}
            cursor = self.varcollection.find({"Nombre": var}, select)
            for data in cursor:
                etiqueta = str(var) + '\t' + data["Etiqueta"].split('.')[0]
                print(etiqueta)

variables = ["CIIU4", "I3R2C1", "I3R2C2", "TIPOLO", "IV1R11C2"]

# ... grafico 8 - inovaciones aspectos de la empresa
for i in range(1,16):
    var = "I2R"+str(i)+"C1"
    variables.append(var)

# ... grafico 6: metodo o tecnica llavadas a cabo por tipo de metodo
variables.append("I1R4C1")
variables.append("I1R4C2")
variables.append("I1R5C1")
variables.append("I1R5C2")
variables.append("I1R6C1")
variables.append("I1R6C2")

# ... inovaciones de productos de la empresa por nivel de alcanca (para la empresa, nacional, internacional)
variables.append("I1R1C1N")
variables.append("I1R1C2N")
variables.append("I1R2C1N")
variables.append("I1R2C2N")
variables.append("I1R3C1N")
variables.append("I1R3C2N")

# total de inovaciones
variables.append("I1R4C2N")

# ... inovaciones de productos de la empresa mejorados por nivel de alcance (para la empresa, nacional, internacional)
variables.append("I1R1C1M")
variables.append("I1R1C2M")
variables.append("I1R2C1M")
variables.append("I1R2C2M")
variables.append("I1R3C1M")
variables.append("I1R3C2M")

# total total de mejorados
variables.append("I1R4C2M")

# grafica 9 - obstaculos para innovar - grafica 10 aplica las mismas respuestas para las TIPOLO INTENC
for i in range(1, 15):
    var = "I10R"+str(i)+"C1"
    variables.append(var)

# graficas 12-15 - Montos invertidos según actividad cientifica, tecnologia o innovacion 2016
for i in range(1, 11):
    var = "II1R"+str(i)+"C2"
    variables.append(var)

# ... III1R1C2
for i in range(1, 4):
    var = "III1R"+str(i)+"C2"
    variables.append(var)

for i in range(4, 8):
    var = "III1R"+str(i)+"C3"
    variables.append(var)
    var = "III1R"+str(i)+"C4"
    variables.append(var)

var = "III1R8C2"
variables.append(var)

# ... personal ocupado y utilizado en ACTI - 2016

for i in range(1, 11):
    var = "IV1R"+str(i)+"C4"
    variables.append(var)

# ... personal ocupado - 2016
for i in range(1, 11):
    var = "IV1R"+str(i)+"C2"
    variables.append(var)

# ... grafico 32 fuentes internas como origen para la inovacion V1R8C1
for i in range(1, 9):
    var = "V1R"+str(i)+"C1"
    variables.append(var)

# ... grafico 33 fuentes externas como origen para la inovacion V1R9C1
for i in range(9, 33):
    var = "V1R"+str(i)+"C1"
    variables.append(var)

# ... grafico 34 relacion de apoyo para realizacion ACTI V2R1C1
for i in range(1, 20):
    var = "V2R"+str(i)+"C1"
    variables.append(var)

print(variables)
expo = Exporter()
expo.exportToCSV(variables)
expo.getVarLabels(variables)

