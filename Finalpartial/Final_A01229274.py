def divide_matriculas(List):
    newList = [[], []]
    for word in List:
        word = word[::-1]
        if int(word[0]) % 2 == 0:
            word = word[::-1]
            newList[0].append(word)
        else:
            word = word[::-1]
            newList[1].append(word)
    return newList


# c = ["PEMM780912MBCLRR00", "PEMM780912MJCLRR00", "PEMM780912MJCLRR00"]


def frecuencia_entidad(List):
    newList = list()  # matrix
    L = []
    for curp in List:
        curp = list(curp)
        entidad = str(curp[11]) + str(curp[12])
        L.append(entidad)
    return L

# print(frecuencia_entidad(c))

# print(frecuencia_entidad(c))
# frecuencia_entidad(c)


def mezcla_ordenada(List1, List2):
    newList = list()
    L = []
    for i in List1:
        L.append(i)
    for i in List2:
        L.append(i)
    while len(L) > 0:
        newList.append(min(L))
        L.remove(min(L))
    return newList


def ganador_etapa(List1, List2):
    newList = list()
    L = list()  # matrix for work
    for k in range(len(List2)):
        for i in List2:
            L.append(i[0])
            i.remove(i[0])
            if len(L) == len(List1):
                for j in L:
                    if j == min(L):
                        newList.append(co[L.index(j)])
                L = []
    return newList


def cuantas_frases(text):
    text = text.split(".")
    return len(text) - 1


def es_perfecto(num):
    suma = 0
    for i in range(1, num + 1):
        if num % i == 0:
            if i == num:
                suma += 0
            else:
                suma += i
        else:
            suma += 0
    if suma == num:
        return True
    else:
        return False


def cuales_perfectos(List):
    newList = list()
    for i in List:
        num = es_perfecto(i)
        if num == True:
            newList.append(i)
    return newList


#s = [[1,0,1,1,0], [1,0,0,0,0], [1,1,1,1,1]]


def reporte(matrix):
    newList = list()
    for List in matrix:
        days = "LMXJV"
        cont = 0
        cont1 = 0
        for i in List:
            if i == 0:
                newList.append(str(matrix.index(List) + 1) + "-" + days[cont])
            cont += 1
    return newList   # a medias
