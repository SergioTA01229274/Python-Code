def multiplica(x, y):
    if x == 1:
        return y
    elif y == 1:
        return x
    else:
        return y + multiplica(x - 1, y)


def enDescendente(n):
    print(n)
    if n == 0 or n == 1:
        return 0
    else:
        return enDescendente(n - 2)


def sumaHarmonica(n):
    if n == 1:
        return 1
    else:
        return (1 / n) + sumaHarmonica(n - 1)


def cuentaCuantas(palabra, x):
    if len(palabra) > 0:
        if palabra[0] == x:
            return 1 + cuentaCuantas(palabra[1:], x)
        else:
            return cuentaCuantas(palabra[1:], x)
    else:
        return 0


# print(cuentaCuantas("hoooolaa", "o"))


def cuantosDigitos(num):
    if len(num) > 0:
        if num[0] in "1234567890":
            return 1 + cuantosDigitos(num[1:])
    else:
        return 0


# print(cuantosDigitos("1238"))

def vocales(palabra):
    if len(palabra) > 0:
        if palabra[0] in "aeiou":
            return 1 + vocales(palabra[1:])
        else:
            return vocales(palabra[1:])
    else:
        return 0


# print(vocales("hola como estas bien y tu"))


def potencia(x, y):
    if y == 0 or x == 1:
        return 1
    else:
        return x * potencia(x, y - 1)


# print(potencia(4,4))


def sumaArregloR(lista):
    if len(lista) > 1:
        if lista[1]:
            lista[0] = lista[0] + lista[1]
            lista.remove(lista[1])
            return sumaArregloR(lista)
        else:
            return lista[0]
    else:
        return lista[0]


# print(sumaArregloR([1,2,3,4,5,6]))


def mcd(x, y):
    print(x, y)
    if x % y == 0:
        return y
    else:
        return mcd(y, x % y)


# print(mcd(258, 312))


def elMayor(lista):
    print(lista)
    if len(lista) > 1:
        if lista[0] < lista[1]:
            lista.remove(lista[0])
            return elMayor(lista)
        else:
            lista.remove(lista[1])
            return elMayor(lista)
    else:
        return lista[0]


# print(elMayor([1, 3432, 54, 33456, 32235, 324, 4556678, 54, 23, 4]))
