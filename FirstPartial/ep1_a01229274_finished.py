import math
def funcion(x):
    x1 = 1 - (x - 1)**2
    x2  = math.sqrt(x - 2)
    if x <= 2: 
        return x1
    elif x > 2: 
        return x2
def riesgo(UV):
    riesgo = "Riesgo"
    TiempoMax = 0
    if UV >= 0 and UV < 3: 
        riesgo = "Bajo"
        TiempoMax = "Mas de 60 minutos"
        print("El riesgo es: ", riesgo)
        print("El tiempo maximo de exposicion es: ", TiempoMax)
    elif UV >= 3 and UV < 6: 
        riesgo = "Moderado"
        TiempoMax = "45 minutos"
        print("El riesgo es: ", riesgo)
        print("El tiempo maximo de exposicion es: ", TiempoMax)
    elif UV >= 6 and UV < 7: 
        riesgo = "Alto"
        TiempoMax = "30 minutos"
        print("El riesgo es: ", riesgo)
        print("El tiempo maximo de exposicion es: ", TiempoMax)
    elif UV >= 7 and UV < 10: 
        riesgo = "Muy Alto"
        TiempoMax = "25 minutos"
        print("El riesgo es: ", riesgo)
        print("El tiempo maximo de exposicion es: ", TiempoMax)
    elif UV >= 10: 
        riesgo = "Extremo"
        TiempoMax = "10 minutos"
        print("El riesgo es: ", riesgo)
        print("El tiempo maximo de exposicion es: ", TiempoMax)
    return UV
def encripta(cadena):
    cadena = cadena.lower()
    cadena = cadena.replace("a", "*")
    cadena = cadena.replace("e", "3")
    cadena = cadena.replace("i", "=")
    cadena = cadena.replace("o", "@")
    cadena = cadena.replace("u", ">")
    return cadena
def masvocales(palabra1, palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    vocales1 = palabra1.count("a") + palabra1.count("e") + palabra1.count("i") + palabra1.count("o") + palabra1.count("u")
    vocales2 = palabra2.count("a") + palabra2.count("e") + palabra2.count("i") + palabra2.count("o") + palabra2.count("u")
    if vocales1 > vocales2: 
        return 1 
    elif vocales2 < vocales2: 
        return -1 
    elif vocales1 == vocales2: 
        return 0 
print("Este programa es capaz de ejecutar varias operaciones y funciones")
print("Las pociones son: ")
print("1. Evaluar el valor de x en una funcion compuesta y")
print("2. Calcular el riesgo y tiempo maximo de exposicion a radiacion UV")
print("3. Encriptar una frase o palabra")
print("4. Comparar si una palabra tiene mas vocales que otra\n")
print("Ingrese el numero de opcion que desea ejecutar")

num = int(input("Opcion:"))
if num == 1: 
    print("Ingrese el valor a evaluar")
    value = int(input("Valor de x: "))
    funcion(value)
elif num == 2: 
    print("Ingrese el indice de radiacion UV")
    uv = int(input("Indice UV: "))
    riesgo(uv)
elif num == 3: 
    print("Ingrese la palabra o frase que desea encriptar")
    palabra = str(input("Palabra: "))
    print("Su palabra o frase encriptada es: ")
    print(encripta(palabra))
elif num == 4: 
    print("Ingrese la primera palabra")
    p1 = str(input("Palabra1: "))
    print("Ingrese la segunda palabra para comparar")
    p2 = str(input("Palabra2: "))
    print(masvocales(p1,p2))