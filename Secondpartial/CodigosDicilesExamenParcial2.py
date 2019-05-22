def parking(matrix):
    cont = 0
    result = []
    letter = "abcdefghijklmnopqrstuvwxyz"
    newMatrix = list()
    for i in matrix:
        newMatrix = matrix[cont]
        cont1 = 0
        for j in newMatrix:
            if j == 0:
                result.append(letter[cont] + str([cont1]))
            cont1 += 1
        cont += 1
    return result  # Ejercicio de estacionamiento del exmaen completo


s = [[1, 0, 0, 1], [0, 0, 1, 1]]


def coincidencias(Word1, Word2):
    Word1 = Word1.lower()
    Word2 = Word2.lower()
    Word1 = list(Word1)
    Word2 = list(Word2)
    cont = 0
    result = 0
    if len(Word1) < len(Word2):
        while cont < len(Word1):
            if Word1[cont] == Word2[cont]:
                result += 1
            else:
                break
            cont += 1
    elif len(Word2) < len(Word1):
        while cont < len(Word2):
            if Word2[cont] == Word1[cont]:
                result += 1
            else:
                break
            cont += 1
    else:
        while cont < len(Word1):
            if Word1[cont] == Word2[cont]:
                result += 1
            else:
                break
            cont += 1
    return result  # Ejercicio de comparacion de palabras
# del examen completo
