import matplotlib.pyplot as plt
import csv

path = "../data/export/"
input_files = []
input_files.append(path + "selection_NOINNO.csv")
input_files.append(path + "selection_AMPLIA.csv")
input_files.append(path + "selection_POTENC.csv")
input_files.append(path + "selection_ESTRIC.csv")

labels = {"NOINNO": "No innovadoras", "AMPLIA": "Innovacion amplia", "POTENC": "Potencial", "ESTRIC": "Estrictas"}


class Scatters:
    def __init__(self):
        self.input_files = []
        self.variables = []

    def setInputFiles(self, input):
        self.input_files = input

    def setVariables(self,vars):
        self.variables = vars

    def getSize(self, value):
        if value <= 10:
            return 20
        elif 11 <= value <= 50:
            return 40
        elif 51 <= value <= 200:
            return 80
        elif value > 201:
            return 160

    def getColor(self, str):
        if str == "ESTRIC":
            return "#9b59b6"
        elif str == "AMPLIA":
            return "#3498db"
        elif str == "POTENC":
            return "#e74c3c"
        elif str == "NOINNO":
            return "#2ecc71"

    def getFactors(self, tipo):
        if tipo == "ESTRIC":
            return -1.0,1.0
        elif tipo == "AMPLIA":
            return 1.0, 1.0
        elif tipo == "POTENC":
            return 1.0, -1.0
        elif tipo == "NOINNO":
            return -1.0, -1.0

    def getScatters(self):
        try:
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
                    for row in reader:

                        k1, k2 = self.getFactors(row[1])
                        xx.append(k1*float(row[23]))
                        yy.append(k2*float(row[24]))
                        area.append(self.getSize(int(row[25])))
                        color.append(self.getColor(row[1]))
                        counter += 1

                    color_index += 1
                    print(counter)
                    plt.scatter(xx, yy, s=area, c=color, alpha=0.4, label=labels[row[1]])


        except IOError as ex:
            print(ex)


plots = Scatters()
plots.setInputFiles(input_files)
plots.setVariables([""])
plots.getScatters()

plt.xlabel('Ventas totales 2016 [Billones COP]')
plt.ylabel('Exportaciones 2016 [Billones COP]')
#plt.ylabel('CIIU4')

plt.xlim(-6.0, 6.0)
plt.ylim(-2.0, 2.0)

plt.legend()
plt.grid(True)
plt.show()
