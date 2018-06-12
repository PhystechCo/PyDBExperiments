import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import matplotlib.axis as maxis
import csv
import pandas as pd
import numpy as np

path = "../data/export/"
input_files = []
input_files.append(path + "ccb_selection_AC_1_7210.csv")
input_files.append(path + "ccb_selection_AC_2_7210.csv")
input_files.append(path + "ccb_selection_AC_3_7210.csv")
input_files.append(path + "ccb_selection_AC_4_7210.csv")


class Parallels:
    def __init__(self):
        self.input_files = []
        self.variables = []
        self.data = []

    def setInputFiles(self, input):
        self.input_files = input

    def setVariables(self,vars):
        self.variables = vars

    def getData(self):
        return self.data

    def getParallels(self):

        try:
            self.data.append(['', 'ciiu_0', 'ciiu_1', 'ciiu_2', 'ciiu_3', 'POS'])

            counter = 0
            nfile = 1
            for file in self.input_files:
                with open(file, 'r', encoding='utf-8') as f:
                    reader = csv.reader(f, dialect="excel-tab")
                    next(reader, None)

                    for row in reader:

                        if nfile == 1:
                            self.data.append([counter,
                                              float(row[2]),
                                              float(row[3]),
                                              float(row[4]),
                                              float(row[5]),
                                              float(nfile)])
                        elif nfile == 2:
                            self.data.append([ counter,
                                               float(row[3]),
                                               float(row[2]),
                                               float(row[4]),
                                               float(row[5]),
                                               float(nfile)])
                        elif nfile == 3:
                            self.data.append([ counter,
                                           float(row[4]),
                                           float(row[2]),
                                           float(row[3]),
                                           float(row[5]),
                                           float(nfile)])

                        elif nfile == 4:
                            self.data.append([counter,
                                               float(row[5]),
                                               float(row[2]),
                                               float(row[3]),
                                               float(row[4]),
                                               float(nfile)])

                        counter += 1

                nfile += 1

            arrdata = np.array(self.data)
            df = pd.DataFrame(data=arrdata[1:, 1:], index= arrdata[1:, 0], columns=arrdata[0, 1:])
            return df

        except IOError as ex:
            print(ex)

parallel = Parallels()
parallel.setInputFiles(input_files)
df = parallel.getParallels()

df.to_csv('../data/export/Dataframe_7210.csv')

plt.figure()

pd.plotting.parallel_coordinates(df[['ciiu_0', 'ciiu_1', 'ciiu_2', 'ciiu_3', 'POS']], 'POS')

plt.show()



