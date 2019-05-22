import os


def clear():
    if os.name == "nt":
        os.system('cls')


def suma(n):
    a = 0
    for i in range(1, n + 1):
        a = a + i
    return a


def sumaResta(n):
    b = 0
    for j in range(1, n + 1):
        if j % 2 == 0:   # Si el contador es par entonces resta dicho termino
            b -= j
        else:
            b += j     # si es inpar entonces lo suma
    return b


def tablaDel(n):
    for k in range(1, 11):
        c = n * k    # Resultado de la multiplicacion del valor ingresado por el contador k
        print(k, "x", n, "=", c)
    return c


def sumaTerminos(n):
    suma = 0      # se crea la variable antes del ciclo para que no se destruya
    for i in range(n):
        suma += int(input("n:"))  # se usa la misma variable que se creo anteriormente como contador
    return suma                   # y se le va sumando las inputs del usuario.


def cuantasVocales(palabra):
    palabra = palabra.lower()
    nvocal = 0
    cont = 0
    while cont < len(palabra):
        vocal = palabra[cont] # los strings son listas de caracteres, la variable vocal es la que va recorriendo el string con la variable cont.
        if vocal == "a" or vocal == "e":
            nvocal += 1
        elif vocal == "i" or vocal == "o":
            nvocal += 1
        elif vocal == "u":
            nvocal += 1
        else:
            nvocal += 0
        cont += 1
    return nvocal


def masVocales(palabra1, palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    nvocal1 = 0
    cont1 = 0
    while cont1 < len(palabra1):
        vocal = palabra1[cont1]
        if vocal == "a" or vocal == "e":
            nvocal1 += 1
        elif vocal == "i" or vocal == "o":
            nvocal1 += 1
        elif vocal == "u":
            nvocal1 += 1
        else:
            nvocal1 += 0
        cont1 += 1
    nvocal2 = 0
    cont2 = 0
    while cont2 < len(palabra2):
        vocal = palabra2[cont2]
        if vocal == "a" or vocal == "e":
            nvocal2 += 1
        elif vocal == "i" or vocal == "o":
            nvocal2 += 1
        elif vocal == "u":
            nvocal2 += 1
        else:
            nvocal2 += 0
        cont2 += 1
    if nvocal1 < nvocal2:
        print(palabra2, "tiene mas vocales que", palabra1)
    elif nvocal1 == nvocal2:
        print("Las palabras tienen la misma cantidad de vocales")
    else:
        print(palabra1, "tiene mas vocales que", palabra2)
    return nvocal1, nvocal2


def reemplazar(x, y, palabra):
    palabra = palabra.lower()
    x = x.lower()
    y = y.lower()
    palabraNew = []
    cont = 0
    while cont < len(palabra):
        letra = palabra[cont]
        palabraNew.insert(cont, letra)
        if palabraNew[cont] == x:
            palabraNew[cont] = y
        elif palabraNew[cont] == " ":
            palabraNew[cont] = " "
        cont += 1
    print("La palabra reemplazada es: ")
    return palabraNew


def retoTriangulo(n):
    x = []
    cont = 0
    while cont < n:
        x.insert(cont, "*")
        y = "".join(x)
        print (y)
        cont += 1

# Hacer funciones compara y separador


print("Este programa hace una gran variedad de cosas")
print("Seleccione que desea hacer")
print("1. Saber el resultado de una serie de numeros que se suman")
print("2. Saber el resultado de una serie de numeros que se suman y restan")
print("3. Saber cual es la tabla de multiplicacion de un numero ")
print("4. Saber cuantas vocales tiene una palabra")
print("5. Saber si una palabra tiene mas vocales que otra")
print("6. Sumar varios terminos y conocer su resultado")
print("7. Reemplazar ciertas letras por otras en una palabra")
print("8. Hacer un triangulo de magnitud variable")
print("*Por favor teclee el numero de opcion solamente")

selec = int(input("Seleccion: "))

if selec == 1:
    clear()
    print("Cuantos terminos desea sumar?")
    a = int(input("Terminos: "))
    print(suma(a))
elif selec == 2:
    clear()
    print("De cuantos terminos desea la serie?")
    b = int(input("Cantidad:"))
    print(sumaResta(b))
elif selec == 3:
    clear()
    print("De que numero desea la tabla de multiplicar?")
    c = int(input("numero:"))
    print(sumaResta(c))
elif selec == 4:
    clear()
    print("Ingrese la palabra de la cual desea verificar las vocales")
    d = input("palabra:")
    print(cuantasVocales(d))
elif selec == 5:
    clear()
    print("Ingrese las palabras en las que desea comparar cantidad de vocales")
    e = input("Palabra1: ")
    f = input("Palabra2: ")
    print(masVocales(e, f))
elif selec == 6:
    clear()
    print("Ingrese cuantos terminos desea sumar")
    g = int(input("Cantidad: "))
    print(sumaTerminos(g))
elif selec == 7:
    clear()
    print("Ingrese que letra desea reemplazar")
    h = input("Letra vieja: ")
    print("Ingrese por que letra desea reemplazarla")
    i = input("Letra nueva: ")
    print("Ingrese la palabra en la que desea hacer el reemplazo")
    j = input("Palabra o frase:")
    print("".join(reemplazar(h, i, j)))
elif selec == 8:
    clear()
    print("Ingrese la cantidad de unidades que desea ensu triangulo")
    k = int(input("Cantidad: "))
    print(retoTriangulo(k))
