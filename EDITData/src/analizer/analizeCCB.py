from pymongo import MongoClient
import json
import csv

BILLION = 1000000000
TIPOLO = {"RD1": 1, "RD2": 2, "RD3": 3, "RD4": 4}

class Exporter:

    def __init__(self):
        """clase que exporta los resultados afiliados CCB DB"""
        with open('../config/dbconfig.json', 'r') as f:
            config = json.load(f)
            dburl = config['DEV']['DBURL']
            dbport = int(config['DEV']['DBPORT'])
            self.client = MongoClient(dburl, dbport)

        self.db = self.client.phystech
        self.collection = self.db.ccbafiliados

    def getProjections(self, findexp, paramlist):
        select = {key: 1 for key in paramlist}
        select["_id"] = 0
        return self.collection.find(findexp, select)

    def exportToCSV(self, vars):
        print("export to CSV")

        for key, value in TIPOLO.items():
            try:

                findex = dict()
                findex['ciiu_' + str(value)] = {"$regex": ".*7210.*"}
                print(findex)

                filename = 'ccb_selection_' + key + '.csv'
                path = "../data/export/" + filename

                with open(path, 'w', encoding='utf-8', newline='') as f:
                    writer = csv.writer(f, dialect="excel-tab")
                    cursor = self.getProjections(findex, vars)

                    headers = cursor.next()
                    header = []
                    for hd in headers:
                        header.append(hd)

                    writer.writerow(header)

                    for data in cursor:
                        row=[]
                        for itr, val in data.items():
                            row.append(val)

                        writer.writerow(row)
                f.close()

            except IOError:
                print("cannot write file")


variables = ['razon_social', 'nit_cc', 'ciiu_1', 'ciiu_2', 'ciiu_3', 'ciiu_4',
             'valor_activo_corriente', 'valor_total_activo_bruto', 'valor_activo_sin_ajuste',
             'valor_ingresos_actividad_ordinaria', 'valor_otros_gastos', 'valor_costo_ventas',
             'valor_gastos_operacionales', 'valor_activo_no_corriente', 'valor_pasivo_corriente',
             'valor_pasivo_no_corriente', 'valor_total_pasivo', 'valor_patrimonio', 'valor_total_pasivo_patrimonio',
             'valor_costo_ventas', 'valor_utilidad_operacional', 'valor_utilidad_neta']

print(variables)
expo = Exporter()
expo.exportToCSV(variables)
