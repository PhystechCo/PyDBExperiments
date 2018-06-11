import csv
from pymongo import MongoClient
import logging
import json


class Code:
    def __init__(self):
        self.seccion = ''
        self.seccion_descripcion = ''
        self.division = ''
        self.division_descripcion = ''
        self.grupo = ''
        self.grupo_descripcion = ''
        self.clase = ''
        self.descripcion = ''

    def setSeccion(self, seccion):
        self.seccion = seccion

    def setSecDescripcion(self, descripcion):
        self.seccion_descripcion = descripcion

    def setDivision(self, division):
        self.division = division

    def setDivDescripcion(self, descripcion):
        self.division_descripcion = descripcion

    def setGrupo(self, grupo):
        self.grupo = grupo

    def setGrupoDescripcion(self, descripcion):
        self.grupo_descripcion = descripcion

    def setClase(self, clase):
        self.clase = clase

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def __str__(self):
        return self.clase + ' ' + self.descripcion


class CIIUUploader:

    def __init__(self):
        """clase que sube los parametros encuesta DANE en nuestra DB"""
        with open('src/config/dbconfig.json', 'r') as f:
            config = json.load(f)
            dburl = config['DEV']['DBURL']
            dbport = int(config['DEV']['DBPORT'])
            self.client = MongoClient(dburl, dbport)

        self.codes = []
        self.info = {}

        self.db = self.client.phystech
        self.collection = self.db.ciiucodes
        result = self.collection.delete_many({})
        logging.basicConfig(filename='src/logs/uploader.log',
                            level=logging.DEBUG,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%m-%d-%y %H:%M')
        logging.debug(result)

    def uploarResultfromCSV(self, csvfile):

        counter = 0

        with open(csvfile, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, dialect="excel-tab")
            for row in reader:

                counter += 1

                col_one = str(row[0])
                group = str(row[1])
                clase = str(row[2])
                description = str(row[3])

                if col_one.startswith("S"):
                    self.info = {}
                    self.info['SEC'] = col_one
                    self.info['SECDESC'] = description
                elif col_one.isdigit():
                    self.info['DIV'] = col_one
                    self.info['DIVDESC'] = description
                elif col_one == '' and group.isdigit():
                    self.info['GR'] = group
                    if clase != '':
                        code = Code()
                        code.setSeccion(self.info['SEC'])
                        code.setSecDescripcion(self.info['SECDESC'])
                        code.setDivision(self.info['DIV'])
                        code.setDivDescripcion(self.info['DIVDESC'])
                        code.setGrupo(self.info['GR'])
                        code.setGrupoDescripcion('')
                        code.setClase(clase)
                        code.setDescripcion(description)
                        self.codes.append(code.__dict__)
                    else:
                        self.info['GRDESC'] = description
                elif col_one == '' and clase.isdigit():
                    code = Code()
                    code.setSeccion(self.info['SEC'])
                    code.setSecDescripcion(self.info['SECDESC'])
                    code.setDivision(self.info['DIV'])
                    code.setDivDescripcion(self.info['DIVDESC'])
                    code.setGrupo(self.info['GR'])
                    code.setGrupoDescripcion(self.info['GRDESC'])
                    code.setClase(clase)
                    code.setDescripcion(description)
                    self.codes.append(code.__dict__)

        for code in self.codes:
            print(code)
            obj_id = self.collection.insert_one(code)
            logging.info('Total data read \t' + str(obj_id) + '\t' + str(code))

