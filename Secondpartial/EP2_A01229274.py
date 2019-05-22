def coincidencias(Word1, Word2):
    Word1 = Word1.lower()
    Word2 = Word2.lower()
    Word1 = list(Word1)
    Word2 = list(Word2)
    cont = 0
    result = 0
    for i in Word1 and Word2:
        if i == Word1[cont] and i == Word2[cont]:
            result += 1
        cont += 1
    return result


def divide(Lista):
    result = []
    minValues = []
    for i in range(3):
        x = min(Lista)
        minValues.append(x)
        Lista.remove(x)
    result.append(minValues)
    result.append(Lista)
    return result


def valida_con_rango(msg, Min, Max):
    while True:
        dato = input(msg)
        try:
            dato = int(dato)
            if dato >= Min and dato <= Max:
                print(True)
                break
        except ValueError:
            print("El dato no es un numero entero")


def cuantosVacios(matrix):
    newMatrix = list()
    result = 0
    cont = 0
    for i in matrix:
        newMatrix = matrix[cont]
        for j in newMatrix:
            if j == 0:
                result += 1
            else:
                result += 0
        cont += 1
    return result
