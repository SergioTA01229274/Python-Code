def valida_num(message):
    while True:
        data = input(message + ": ")
        try:
            data = int(data)
            return data
        except ValueError:
            print("El dato no pude ser transformado a entero.")
            print("Intentelo de nuevo")


def mayor_Ingresado():
    listW = list()
    data = 1
    while data > 0:
        data = valida_num("Ingrese  un dato")
        listW.append(data)
    return max(listW)


# s = ["hola.py", "hola.txt", "holas.txt", "hoola.docx", "g.txt", "g.py", "f.txt", "p.py", "r.docx", "k.txt"]


def extension_frecuente(List):
    newList = [0, 0, 0]
    for i in List:
        components = i.split(".")
        if components[1] == "txt":
            newList[0] += 1
        elif components[1] == "docx":
            newList[1] += 1
        elif components[1] == "py":
            newList[2] += 1
    if newList[0] == max(newList):
        return ".txt"
    elif newList[1] == max(newList):
        return ".docx"
    elif newList[2] == max(newList):
        return ".py"

# w = [1, 2, 3, 4, 5, 6, 7, 8]


def duplica_lista(List):
    newList = list()
    for i in range(2):
        for j in List:
            newList.append(j)
    return newList


# g = ["paco", "sergio", "nat", "jorge", "luis"]
# y = [[12, 123, 4523, 23, 43], [23, 234, 31, 234, 4], [32, 23, 43, 54, 55], [432, 1, 43, 54, 6], [34, 54, 35, 34, 554]]


def ganador(List1, List2):
    newList = list()
    for List in List2:
        suma = 0
        for j in List:
            suma += j
        newList.append(suma)
        suma = 0
    winner = newList.index(min(newList))
    return List1[winner]


# t = "En el subterraneo habia un subagente de bienes suburbanos."
# pre = "sub"


def con_prefijo(text, pre):
    text = text.lower()
    textW = text.split(" ")
    newList = list()
    for word in textW:
        cont1 = 0
        cont = 0
        while True:
            if word[cont] == pre[cont]:
                cont1 += 1
                if cont1 == len(pre):
                    newList.append(word)
                    break
            else:
                break
            cont += 1
    return newList


def nomenclatura(building, floors, apartments):
    newList = list()
    for i in range(floors):
        List = []
        for j in range(1, apartments + 1):
            if j < 10:
                List.append(str(building + str(i) + "-" + str(0) + str(j)))
            else:
                List.append(str(building + str(i) + "-" + str(j)))
        newList.append(List)
    return newList
