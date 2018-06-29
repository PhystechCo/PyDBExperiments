import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np

from src.analizer.Utilities import *
from src.analizer.Constants import *

path = "../data/export/"
input_files = []
input_files.append(path + "selection_NOINNO.csv")
input_files.append(path + "selection_AMPLIA.csv")
input_files.append(path + "selection_POTENC.csv")
input_files.append(path + "selection_ESTRIC.csv")
input_files.append(path + "selection_INTENC.csv")

input_files_inno = []
input_files_inno.append(path + "selection_AMPLIA.csv")
input_files_inno.append(path + "selection_POTENC.csv")
input_files_inno.append(path + "selection_ESTRIC.csv")

input_files_amplia = []
input_files_amplia.append(path + "selection_AMPLIA.csv")


class Scatters:
    def __init__(self):
        self.input_files = []
        self.variables = []

    def getGroup(self, ciiu):
        for key, value in industries.items():
            if value[1] <= ciiu < value[2]:
                return value[0]

    def initGroups(self, max):
        container = {}
        for i in range(1, 25):
            container[i] = 0
        return container

    def setInputFiles(self, input):
        self.input_files = input

    def setVariables(self,vars):
        self.variables = vars

    def getAnalysisOne(self):
        try:

            n_inno_empresa = 0
            n_inno_mejorados_nacional = 0
            n_inno_inter = 0

            n_inno_empresa_mejor = 0
            n_inno_mejorados_nacional_mejor = 0
            n_inno_inter_mejor = 0

            for file in self.input_files:
                with open(file, 'r', encoding='utf-8') as f:
                    reader = csv.reader(f, dialect="excel-tab")
                    next(reader, None)
                    counter = 0
                    xx = []
                    yy = []
                    area = []
                    color = []
                    color_index = 0

                    group_numbers = self.initGroups(25)

                    test = 0

                    for row in reader:

                        ciiu = int(row[0])
                        group = self.getGroup(ciiu)
                        group_numbers[group] += 1

                        if 2600 <= ciiu < 2700:
                            test += 1

                        # ... I1R1C1N
                        inno_empresa = int(row[2])
                        n_inno_empresa += int(row[3])

                        # ... I1R2C1N
                        inno_mejorados_nacional = int(row[4])
                        n_inno_mejorados_nacional += int(row[5])

                        # ... I1R3C1N
                        inno_empresa_inter = int(row[6])
                        n_inno_inter += int(row[7])

                        # ... I1R1C1N
                        inno_empresa_mejor = int(row[9])
                        n_inno_empresa_mejor += int(row[10])

                        # ... I1R2C1N
                        inno_mejorados_nacional_mejor = int(row[11])
                        n_inno_mejorados_nacional_mejor += int(row[12])

                        # ... I1R3C1N
                        inno_empresa_mejor = int(row[13])
                        n_inno_inter_mejor += int(row[14])

                        k1, k2 = getFactors(row[1])
                        xx.append(k1*float(row[37]))
                        yy.append(k2*float(row[38]))
                        area.append(getSize(int(row[95])))
                        color.append(getColor(row[1]))
                        counter += 1

                    color_index += 1
                    print(counter)
                    plt.scatter(xx, yy, s=area, c=color, alpha=0.4, label=labels[row[1]])

                    for key in group_numbers:
                        print(str(key) + '\t' + str(group_numbers[key]))

                    print("****" + str(test))

            results_nuevos = str(n_inno_empresa) + '\t' + str(n_inno_mejorados_nacional) + '\t' + str(n_inno_inter)
            results_mejor = str(n_inno_empresa_mejor) + '\t' + str(n_inno_mejorados_nacional_mejor) + '\t' + str(n_inno_inter_mejor)
            print(results_nuevos)
            print(results_mejor)

        except IOError as ex:
            print(ex)

    def getAnalysisTwo(self):
        try:

            for file in self.input_files:

                inversion_acti = []
                obstaculos_acti = []
                importancia_acti = []
                obstaculos_nulos_acti = []
                importancia_nulos__acti = []

                for idx in range(0,20):
                    inversion_acti.append(0.0)
                    obstaculos_acti.append(0.0)
                    importancia_acti.append(0.0)
                    obstaculos_nulos_acti.append(0.0)
                    importancia_nulos__acti.append(0.0)

                with open(file, 'r', encoding='utf-8') as f:
                    reader = csv.reader(f, dialect="excel-tab")
                    next(reader, None)
                    counter = 0
                    xx = []
                    yy = []
                    area = []
                    color = []
                    color_index = 0
                    total_invertido_2016 = 0.0

                    for row in reader:
                        total_invertido_2016 += float(row[62])
                        for idx in range(0, 9):
                            inversion_acti[idx] += float(row[idx+53])

                        for idx in range(0,13):
                            if row[idx+39] == '1':
                                obstaculos_acti[idx] += 1.0
                            elif row[idx+39] == '3':
                                obstaculos_nulos_acti[idx] += 1.0

                        for idx in range(0, 14):
                            if row[idx+22] == '1':
                                importancia_acti[idx] += 1.0
                            elif row[idx+22] == '3':
                                importancia_nulos__acti[idx] += 1.0

                    #... color_index += 1
                    #... plt.scatter(xx, yy, s=area, c=color, alpha=0.6, label=labels[row[1]])
                    print(str(total_invertido_2016/BILLON))
                    for idx in range(0, 9):
                        info = "* " + totales_inversion_ACTI[idx+53] + '\t' + str(inversion_acti[idx])
                        print(info)

                    print("")
                    print("")

                    for idx in range(0, 13):
                        info = "** " + obstaculos[idx+39] + '\t' + str(obstaculos_acti[idx]) + '\t' + str(obstaculos_nulos_acti[idx])
                        print(info)

                    print("")
                    print("")

                    for idx in range(0, 14):
                        info = "*** " + importancia_innovaciones[idx+22] + '\t' + str(importancia_acti[idx]) + '\t' + str(importancia_nulos__acti[ idx ])
                        print(info)

        except IOError as ex:
            print(ex)


    def getAnalysisThree(self):
        try:

            for file in self.input_files:
                with open(file, 'r', encoding='utf-8') as f:
                    reader = csv.reader(f, dialect="excel-tab")
                    next(reader, None)

                    for row in reader:

                        # ... Motivacion
                        criteria_1 = int(row[27])
                        criteria_2 = int(row[22])
                        criteria_3 = int(row[26])

                        # ... Obstaculos
                        criteria_4 = int(row[47])
                        criteria_5 = int(row[40])
                        criteria_6 = int(row[45])

                        sum_all = criteria_1 + criteria_2 + criteria_3 + criteria_4 + criteria_5 + criteria_6

                        if sum_all == 6:
                            print(row[0])

        except IOError as ex:
            print(ex)


anal = 3

if anal == 1:
    plots = Scatters()
    plots.setInputFiles(input_files)
    plots.setVariables([""])
    plots.getAnalysisOne()
    plt.xlabel('Ventas totales 2016 [Billones COP]')
    plt.ylabel('Exportaciones 2016 [Billones COP]')
    plt.xlim(-0.5, 0.5)
    plt.ylim(-0.5, 0.5)
    plt.legend()
    plt.grid(True)
    plt.show()

elif anal == 2:
    plots = Scatters()
    plots.setInputFiles(input_files_inno)
    plots.setVariables([""])
    plots.getAnalysisTwo()
    #... plt.xlabel('Nivel de calificación')
    #... plt.ylabel('Nivel de inversión en ACTI')
    #... plt.xlim(0, 11)
    #... plt.ylim(0, 11)
    #... plt.legend()
    #... plt.grid(True)
    #... plt.show()

elif anal == 3:
    print("Analisis 3")
    plots = Scatters()
    plots.setInputFiles(input_files_amplia)
    plots.setVariables([""])
    plots.getAnalysisThree()

