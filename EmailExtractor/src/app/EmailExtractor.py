import re
import csv
import os

from .Email import Email


class EmailExtractor:

    def __init__(self):
        self.addresses = dict()
        self.addresses_date = []

    def extractAddresses(self, msgdir):
        try:

            directory = os.fsencode(msgdir)

            for file in os.listdir(directory):
                inputfile = msgdir + os.fsdecode(file)
                email_date = os.fsdecode(file).split('-')[0]

                with open(inputfile, 'r', encoding='utf-8') as infile:
                    for line in infile:
                        result = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", line)
                        for em in result:
                            self.addresses[em] = self.addresses.get(em, 0) + 1
                            self.addresses_date.append(em + ',' + email_date)

        except IOError as exception:
            print(exception)

    def exportAddresses(self):

        try:
            path = "app/data/export/extracted-emails.csv"
            with open(path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f, dialect="excel", delimiter=';')

                for key, value in self.addresses.items():
                    row = []
                    row.append(key.lower())
                    domain = key.split('@')[1]
                    row.append(domain.lower())
                    row.append(str(value))
                    writer.writerow(row)

            path = "app/data/export/extracted-emails_with_date.csv"
            with open(path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f, dialect="excel", delimiter=';')

                for value in self.addresses_date:
                    data = value.split(',')
                    row = []
                    row.append(data[0].lower())
                    domain = data[0].split('@')[1]
                    row.append(domain.lower())
                    row.append(str(data[1]))
                    writer.writerow(row)

        except IOError as exception:
            print(exception)

