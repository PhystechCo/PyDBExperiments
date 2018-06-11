import csv
from pymongo import MongoClient
import logging
import json


class Parameter:
    def __init__(self):
        self.ID = ''
        self.Nombre = ''
        self.Etiqueta = ''
        self.Tipo = ''
        self.Formato = ''
        self.Pregunta = ''

    def setID(self, id):
        self.ID = id

    def setNombre(self, nombre):
        self.Nombre = nombre

    def setEtiqueta(self, etiqueta):
        self.Etiqueta = etiqueta

    def setTipo(self, tipo):
        self.Tipo = tipo

    def setFormato(self, formato):
        self.Formato = formato

    def setPregunta(self, pregunta):
        self.Pregunta = pregunta

    def appendEtiqueta(self,txt):
        self.Etiqueta += ' ' + txt

    def appendPregunta(self,txt):
        self.Pregunta += ' ' + txt

    def __str__(self):
        return self.ID + ' ' + self.Etiqueta


class ParametersUploader:

    def __init__(self):
        """clase que sube los parametros encuesta DANE en nuestra DB"""
        with open('src/config/dbconfig.json', 'r') as f:
            config = json.load(f)
            dburl = config['DEV']['DBURL']
            dbport = int(config['DEV']['DBPORT'])
            self.client = MongoClient(dburl, dbport)

        self.param = None
        self.parameters = []

        self.db = self.client.phystech
        self.collection = self.db.editvariables
        logging.basicConfig(filename='logs/uploader.log',
                            level=logging.DEBUG,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%m-%d-%y %H:%M')

    def uploarResultfromCSV(self, csvfile):

        counter = 0

        with open(csvfile, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, dialect="excel-tab")
            for row in reader:

                batch = []
                txt = ''.join(row)
                id = row[0].rstrip()

                if txt == '':
                    continue
                elif txt == 'IDNombreEtiquetaTipoFormatoPregunta':
                    continue
                elif txt == 'COLOMBIA - Encuesta de Desarrollo e Innovacion Tecnologica - EDIT- Industria VIII - 2015 - 2016':
                    continue

                if id.isdigit():
                    continue
                elif id != '':
                    self.param = Parameter()
                    self.param.setID(id)
                    self.param.setNombre(row[1])
                    self.param.setEtiqueta(row[2])
                    self.param.setTipo(row[3])
                    self.param.setFormato(row[4])
                    self.param.setPregunta(row[5])
                    self.parameters.append(self.param)
                    counter += 1
                else:
                    self.param.appendEtiqueta(row[2])
                    self.param.appendPregunta(row[5])

        print(counter)
        for param in self.parameters:
            obj_id = self.collection.insert_one(param.__dict__)
            logging.info('Total data read \t' + str(obj_id) + '\t' + str(param))

    def getProjections(self, paramlist):
        select = {key: 1 for key in paramlist}
        select["_id"] = 0
        return self.collection.find({}, select)

    def exportResultsCSV(self, variables):
        counter = 0
        try:

            filename = 'variables_table.csv'
            path = "src/data/export/" + filename

            with open(path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f, dialect="excel-tab")
                cursor = self.getProjections(variables)

                for data in cursor:
                    row = []
                    for itr, val in data.items():
                        row.append(val)

                    writer.writerow(row)

            f.close()

        except IOError:
            print("cannot write file")

