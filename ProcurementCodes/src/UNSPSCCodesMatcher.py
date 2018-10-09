from pymongo import MongoClient
import logging


class UNSPSCCodeMatcher:
    def __init__(self):
        """clase que crea realiza el matching entre los materiales existentes y los codigos UNSPSC"""
        dev = False
        dburl = 'localhost'
        dport = 27017
        self.client = MongoClient(dburl, dport)
        self.db = self.client.conpancol
        self.unspsccodes = self.db.unspsccodes

        logging.basicConfig(filename='logs/matcher.log',
                            level=logging.DEBUG,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%m-%d-%y %H:%M')

    def getProjections(self, paramlist):
        select = {key: 1 for key in paramlist}
        select["_id"] = 0
        return self.unspsccodes.find({}, select)

    def match(self):

        vars = ['itemcode', 'category', 'type']

        cursor = self.getProjections(vars)

        for data in cursor:
            print(data)

