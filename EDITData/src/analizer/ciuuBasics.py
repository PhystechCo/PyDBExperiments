import csv
import matplotlib.pyplot as plt
import numpy as np

MILMILLONES = 1000000000
BILLON = 1000*MILMILLONES


def getSize(str):
    value = float(str)
    if value <= 50:
        return 10
    elif 51 <= value <= 200:
        return 50
    elif value > 200:
        return 200


def getHistogram(filename):
    try:
        for file in filename:
            with open(file, 'r', encoding='utf-8') as f:
                reader = csv.reader(f, dialect="excel-tab")
                next(reader, None)
                counter = 0
                xx = []
                section = []
                manu = []

                for i in range(0, 21):
                    section.append(0)

                ingresos_totales = 0.0

                for row in reader:

                    x1 = float(row[2])

                    if 7209.99 >= x1 >= 7211.0:
                        continue

                    try:
                        x2 = float(row[9]) / BILLON
                        if x2 > 0:
                            ingresos_totales += x2
                    except:
                        print("0.0 income")

                    xx.append(x1)
                    counter += 1
                    if 1000 <= x1 <= 3320:
                        section[0] += 1
                        try:
                            x2 = float(row[9])/MILMILLONES
                            if x2 <= 0:
                                continue
                            x3 = getSize(row[21])
                            manu.append([x1, x2, x3])
                        except:
                            print("no value present x2,x3")
                    elif 3330 <= x1 <= 3530:
                        section[1] += 1
                    elif 3600 <= x1 <= 3900:
                        section[2] += 1
                    elif 4100 <= x1 <= 4390:
                        section[3] += 1
                    elif 4500 <= x1 <= 4800:
                        section[4] += 1
                    elif 4900 <= x1 <= 5320:
                        section[5] += 1
                    elif 5500 <= x1 <= 5630:
                        section[6] += 1
                    elif 5800 <= x1 <= 6400:
                        section[7] += 1
                    elif 6410 <= x1 <= 6630:
                        section[8] += 1
                    elif 6800 <= x1 <= 6820:
                        section[9] += 1
                    elif 6900 <= x1 <= 7500:
                        section[10] += 1
                    elif 7710 <= x1 <= 8300:
                        section[11] += 1
                    elif 8400 <= x1 <= 8430:
                        section[12] += 1
                    elif 8500 <= x1 <= 8560:
                        section[13] += 1
                    elif 8600 <= x1 <= 8890:
                        section[14] += 1
                    elif 9000 <= x1 <= 9330:
                        section[15] += 1
                    elif 9400 <= x1 <= 9609:
                        section[16] += 1
                    elif 9700 <= x1 <= 9820:
                        section[17] += 1
                    elif 9900 <= x1 <= 10000:
                        section[18] += 1
                    elif 0 <= x1 <= 322:
                        section[19] += 1
                    elif 500 <= x1 <= 990:
                        section[20] += 1

                num_bins = 40
                print(counter)
                n, bins, patches = plt.hist(xx, num_bins, facecolor='blue', alpha=0.5)

                max_y = 3500

                plt.xlabel('CIUU')
                plt.ylabel('Frecuencia')
                plt.title('CIUU Afiliados CCB')
                plt.axis([0, 9900, 0, max_y])
                plt.grid(True)

                plt.plot([1000,1000], [0,max_y], linestyle='--')
                plt.plot([3320, 3320], [ 0, max_y ], linestyle='--')

                plt.show()

                for val in section:
                    print(val)

                print("-----")

                for val in manu:
                    row = str(val[0]) + '\t' + str(val[1]) + '\t' + str(val[2])
                    print(row)

                print(ingresos_totales)

    except IOError as ex:
        print(ex)


getHistogram(['../data/export/ccb_selection_variables.csv'])

