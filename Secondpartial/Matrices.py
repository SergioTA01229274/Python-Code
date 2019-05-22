def creaMatriz1(n):
    matriz = []
    for i in range(n):
        elements = []
        for i in range(n):
            elements.append(-1)
        matriz.append(elements)
    return matriz


def sumaMatriz(matriz):
    result = 0
    cont = 0
    newList = list()
    for i in range(len(matriz)):
        newList = matriz[cont]
        x = 0
        for j in range(len(newList)):
            result += newList[x]
            x += 1
        cont += 1
    return result


def cambiaNegativos(matrix):
    cont = 0
    newMatrix = list()
    result = []
    for i in range(len(matrix)):
        newMatrix = matrix[cont]
        y = 0
        for j in range(len(newMatrix)):
            if newMatrix[y] < 0:
                newMatrix[y] = 0
            y += 1
        result.append(newMatrix)
        cont += 1
    return result


def busca(matrix, n):
    result = True
    newMatrix = list()
    cont = 0
    for i in matrix:
        newMatrix = matrix[cont]
        for j in newMatrix:
            if j == n:
                result = result
            else:
                result = not result
        cont += 1
    return result


def sumaMayores5(matrix):
    newMatrix = list()
    result = 0
    cont = 0
    for i in matrix:
        newMatrix = matrix[cont]
        for j in newMatrix:
            if j > 5:
                result += j
            else:
                result += 0
        cont += 1
    return result
