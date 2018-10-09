import csv
from .ProcurementCodes import ProcurementCodes
from pymongo import MongoClient
import logging
import re


class CodeUploader:
    def __init__(self):
        """clase que crea PROCUREMENT CODES  en el formator necesario para guardar en la DB"""
        dev = False
        dburl = 'localhost'
        dport = 27017
        self.client = MongoClient(dburl, dport)
        self.db = self.client.conpancol
        self.procurementcodes = self.db.procurementcodes
        self.unspsccodes = self.db.unspsccodes

        logging.basicConfig(filename='logs/pccreator.log',
                            level=logging.DEBUG,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%m-%d-%y %H:%M')

        self.segment_description = ""
        self.family_description = ""
        self.category_description = ""

    def uploadCodefromCSV(self, csvfile):
        with open(csvfile, 'r', encoding='ISO-8859-1', errors='ignore') as f:
            reader = csv.reader(f, dialect="excel-tab")
            nrow = 0

            for row in reader:
                segment = row[0]
                family = row[1]
                category = row[2]
                commodity = row[3]
                locale = row[4]
                description = row[5]

                if family == "00" and category == "00" and commodity == "00":
                    self.segment_description = description
                    continue
                elif category == "00" and commodity == "00":
                    self.family_description = description
                    continue
                else:

                    self.category_description = description

                    code = segment + family + category + commodity

                    item = ProcurementCodes()

                    item.setSegment(segment)
                    item.setFamily(family)
                    item.setCategory(category)
                    item.setCommodity(commodity)
                    item.setCode(code)
                    item.setLocale(locale)
                    item.setDescription(description)
                    item.setSegmentDescription(self.segment_description)
                    item.setFamilyDescription(self.family_description)
                    item.setCategoryDescription(self.category_description)

                    item_json = item.__dict__

                    obj_id = self.procurementcodes.insert_one(item_json)
                    print(obj_id)

                    nrow += 1

    def uploadUNSPSCCodefromCSV(self, csvfile):
        with open(csvfile, 'r', encoding='ISO-8859-1', errors='ignore') as f:
            reader = csv.reader(f)
            next(reader, None)  # skip the headers
            for row in reader:
                segment = row[0]
                self.segment_description = row[1]
                family = row[2]
                self.family_description = row[3]
                category = row[4]
                self.category_description = row[5]
                commodity = row[6]
                description = row[7]
                locale = "EN_US"

                item = ProcurementCodes()

                item.setSegment(segment)
                item.setFamily(family)
                item.setCategory(category)
                item.setCommodity(commodity)
                item.setCode(commodity)
                item.setLocale(locale)
                item.setDescription(description)
                item.setSegmentDescription(self.segment_description)
                item.setFamilyDescription(self.family_description)
                item.setCategoryDescription(self.category_description)

                item_json = item.__dict__

                obj_id = self.unspsccodes.insert_one(item_json)
                print(obj_id)

    def findByCode(self, code, paramlist):
        select = {key: 1 for key in paramlist}
        select["_id"] = 0
        regx = re.compile("^"+code, re.IGNORECASE)
        return self.unspsccodes.find({"code": regx}, select)

    def queryCodes(self, code):

        vars = []
        vars.append('code')
        vars.append('segment_description')
        vars.append('description')
        cursor = self.findByCode(code, vars)

        for ct in cursor:
            print(ct)

