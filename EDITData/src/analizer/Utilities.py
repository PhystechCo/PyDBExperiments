def getSize(value):
    if value <= 10:
        return 20
    elif 11 <= value <= 50:
        return 40
    elif 51 <= value <= 200:
        return 80
    elif value > 201:
        return 160


def getColor(str):
    if str == "ESTRIC":
        return "#9b59b6"
    elif str == "AMPLIA":
        return "#3498db"
    elif str == "POTENC":
        return "#e74c3c"
    elif str == "NOINNO":
        return "#2ecc71"
    elif str == "INTENC":
        return "#ffde57"


def getFactors(tipo):
    if tipo == "ESTRIC":
        return -1.0, 1.0
    elif tipo == "AMPLIA":
        return 1.0, 1.0
    elif tipo == "POTENC":
        return 1.0, -1.0
    elif tipo == "NOINNO":
        return -1.0, -1.0
    elif tipo == "INTENC":
        return -1.0, -1.0
