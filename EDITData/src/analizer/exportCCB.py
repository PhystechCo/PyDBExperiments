from pymongo import MongoClient
import json
import csv

ACTIVITY = 7210
TIPOLO = {"AC_1_7210": 1, "AC_2_7210": 2, "AC_3_7210": 3, "AC_4_7210": 4}


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

    def getIndexedProjections(self, findexp, paramlist):
        select = {key: 1 for key in paramlist}
        select["_id"] = 0
        return self.collection.find(findexp, select)

    def getProjections(self, paramlist):
        select = {key: 1 for key in paramlist}
        select["_id"] = 0
        return self.collection.find({}, select)

    def exportByActivityToCSV(self, vars):
        print("export to CSV")

        for key, value in TIPOLO.items():
            try:

                findex = dict()
                findex['ciiu_' + str(value)] = ACTIVITY
                print(findex)

                filename = 'ccb_selection_' + key + '.csv'
                path = "../data/export/" + filename

                with open(path, 'w', encoding='utf-8', newline='') as f:
                    writer = csv.writer(f, dialect="excel-tab")
                    cursor = self.getIndexedProjections(findex, vars)

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

    def exportAllToCSV(self, vars):
        print("export to CSV")

        try:

            filename = 'ccb_selection_variables.csv'
            path = "../data/export/" + filename

            with open(path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f, dialect="excel-tab")
                cursor = self.getProjections(vars)

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
             'valor_costo_ventas', 'valor_utilidad_operacional', 'valor_utilidad_neta', 'cnt_pers_ocupado']

print(variables)
expo = Exporter()
if 0:
    expo.exportByActivityToCSV(variables)

else:
    expo.exportAllToCSV(variables)



