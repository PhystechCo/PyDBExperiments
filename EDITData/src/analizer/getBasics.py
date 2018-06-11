from pymongo import MongoClient
import json
import matplotlib.pyplot as plt


class Basics:

    def __init__(self):
        """clase que sube los resultados encuesta DANE en nuestra DB"""
        with open('../config/dbconfig.json', 'r') as f:
            config = json.load(f)
            dburl = config['DEV']['DBURL']
            dbport = int(config['DEV']['DBPORT'])
            self.client = MongoClient(dburl, dbport)

        self.db = self.client.phystech
        self.collection = self.db.editresults

    def getProjection(self, param):
        return self.collection.find({}, {param: 1})

    def getProjections(self, paramlist):
        return self.collection.find({}, {key: 1 for key in paramlist})


def getSize(str):
    value = float(str)
    if value <= 50:
        return 10
    elif 51 <= value <= 200:
        return 50
    elif value > 200:
        return 200


def getColor(str):
    if str == "ESTRIC":
        return "#9b59b6"
    elif str == "AMPLIA":
        return "#3498db"
    elif str == "POTENC":
        return "#e74c3c"
    elif str == "NOINNO":
        return "#2ecc71"


value_I3R2C1=[]
value_I3R2C2=[]

billion = 1000000000

code = "I3R2C1"
basics = Basics()
cursor = basics.getProjection(code)
for ct in cursor:
    value_I3R2C1.append(ct[code]/billion)

code = "I3R2C2"
cursor = basics.getProjection(code)
for ct in cursor:
    value_I3R2C2.append(ct[code]/billion)

svalue = sorted(value_I3R2C1)
print(len(svalue), svalue[0], svalue[-1])

num_bins = 100

plt.subplot(3, 1, 1)
# the histogram of the data
n, bins, patches = plt.hist(value_I3R2C1, num_bins, facecolor='blue', alpha=0.5)

plt.xlabel('Ventas [Billones COP]')
plt.ylabel('Frecuencia')
plt.title('Ventas nacionales 2016')
plt.axis([0, 6.0, 1, 10000])
plt.grid(True)
plt.semilogy()

plt.subplot(3, 1, 2)
# the histogram of the data
n, bins, patches = plt.hist(value_I3R2C2, num_bins, facecolor='blue', alpha=0.5)

plt.xlabel('Ventas [Billones COP]')
plt.ylabel('Frecuencia')
plt.title('Exportaciones 2016')
plt.axis([0, 6.0, 1, 10000])
plt.grid(True)
plt.semilogy()

#plt.show()

cursor = basics.getProjections(["I3R2C1", "I3R2C2", "TIPOLO", "IV1R11C2"])
code = "IV1R11C2"
personal = []
for ct in cursor:
    personal.append(ct[code])

plt.subplot(3, 1, 3)
n, bins, patches = plt.hist(personal, num_bins, facecolor='blue', alpha=0.5)

plt.xlabel('N')
plt.ylabel('')
plt.title('Personal ocupado promedio 2016')
plt.axis([0, 6000.0, 1, 10000])
plt.grid(True)
plt.semilogy()
plt.show()

###Prepare data
xx = []
yy = []
color = []
size = []

cursor = basics.getProjections(["I3R2C1", "I3R2C2", "TIPOLO", "IV1R11C2"])

for ct in cursor:
    if ct["TIPOLO"] != "INTENC":
        occupied = float(ct["IV1R11C2"])
        if occupied == 0:
            continue
        if occupied < 100:
            continue
        nat_sales = ct["I3R2C1"]/billion
        int_sales = ct["I3R2C2"]/billion
        if nat_sales > 1.0 or int_sales > 0.4:
            continue
        xx.append(nat_sales)
        yy.append(int_sales)
        occupied = ct["IV1R11C2"]
        tipo = ct["TIPOLO"]
        color.append(getColor(tipo))
        size.append(getSize(occupied))



plt.scatter(xx, yy, s=size, c=color, alpha=0.5)
plt.xlabel('Ventas Nacionales 2016 [Billones COP]')
plt.ylabel('Exportaciones 2016 [Billones de COP]')
plt.text(0.8, 0.40, 'ESTRIC', fontsize=10, color="#9b59b6")
plt.text(0.8, 0.38, 'AMPLIA', fontsize=10, color="#3498db")
plt.text(0.8, 0.36, 'POTENC', fontsize=10, color="#e74c3c")
plt.text(0.8, 0.34, 'NOINNO', fontsize=10, color="#2ecc71")
plt.axis([0, 1.0, 0, 0.4])

plt.show()
