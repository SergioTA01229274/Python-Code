# Lista ordenada
# s = [1, 2, 4, 5, 10, 11]


def busqueda_binaria(List, num):
    left = 0
    right = len(List) - 1
    while left <= right:
        middle = (left + right) // 2
        if num == List[middle]:
            return middle
        elif List[middle] > num:
            right = middle - 1
        else:
            left = middle + 1
    return -1


def elimina_duplicados(List):
    newList = list()
    for i in List:
        if i not in newList:
            newList.append(i)
    return newList


def con_duplicados(List):
    newList = list()
    value = False
    for i in List:
        if i not in newList:
            newList.append(i)
            value = False
        else:
            value = True
            if value:
                return value
    return value


def ordenada(List):
    value = False
    while len(List) > 0:
        if List[0] == min(List):
            value = True
        else:
            value = False
            return value
        List.remove(List[0])
    return value


def invierte(List):
    newList = list()
    while len(List) > 0:
        newList.append(List[len(List) - 1])
        List.remove(List[len(List) - 1])
    return newList


# r = "hola como estas yo muy bien y tu no pues algo cansado gracias jaja"


def palabras_con_mas_de(text, num):
    List = text.split(" ")
    cont = 0
    for i in List:
        if len(i) == num:
            cont += 1
    return cont


def espaciado(text):
    newWord = ""
    for i in text:
        if i != " ":
            newWord += i
            newWord += " "
        else:
            newWord += i
    return newWord


# x = [1, 2, 3, 4, 5, 11, 12, 13]
# y = [6, 7, 8, 9, 10]


def combina_listas(List1, List2):
    newList = list()
    if len(List1) == len(List2):
        while len(List1) > 0:
            newList.append(List1[0])
            List1.remove(List1[0])
            newList.append(List2[0])
            List2.remove(List2[0])
    elif len(List1) < len(List2):
        while len(List1) > 0:
            newList.append(List1[0])
            List1.remove(List1[0])
            newList.append(List2[0])
            List2.remove(List2[0])
        while len(List2) > 0:
            newList.append(List2[0])
            List2.remove(List2[0])
    else:
        while len(List2) > 0:
            newList.append(List1[0])
            List1.remove(List1[0])
            newList.append(List2[0])
            List2.remove(List2[0])
        while len(List1) > 0:
            newList.append(List1[0])
            List1.remove(List1[0])
    return newList


def numeros_rango(num1, num2):
    newList = list()
    while True:
        data = int(input("Ingrese un numero: "))
        if data > num1 and data < num2:
            newList.append(data)
        else:
            print("El dato no se encentra en el rango especificado")
            break
    return newList


def numeros_suman(num):
    import random
    suma = 0
    newList = list()
    while suma < num:
        term = random.randint(1, num // 2)
        newList.append(term)
        suma += term
    return newList


# m = [["pato", "pato", "pato", "ganso", "pato", "ganso", "ganso"], ["pato", "ganso", "ganso", "ganso", "pato"], ["pato", "ganso", "ganso", "pato"]]


def cuenta_palabras(matrix, word):
    word = word.lower()
    newList = list()
    cont = 0
    for i in matrix:
        for j in i:
            if j == word:
                cont += 1
        newList.append(cont)
        cont = 0
    return newList


# s = [[12, 11, 3, 5, 10, 25], [1, 5, 20, 30, 11, 4], [2, 5, 20, 15, 4]]


def multiplos_de_5(matrix):
    for List in matrix:
        for j in List:
            if j % 5 != 0:
                List[List.index(j)] = 0
    return matrix


# g = [["casa", "arroz", "coco", "bebe", "juego"], ["eso", "atun", "audifono", "cesar", "boca"], ["zorro", "perro", "ansiedad", "bueno", "bono", "cancion", "mochila"]]


def ordena_ABC(matrix):
    newMatrix = [[], [], [], []]
    for List in matrix:
        for i in List:
            if i[0] == "a":
                newMatrix[0].append(i)
            elif i[0] == "b":
                newMatrix[1].append(i)
            elif i[0] == "c":
                newMatrix[2].append(i)
            else:
                newMatrix[3].append(i)
    return newMatrix
