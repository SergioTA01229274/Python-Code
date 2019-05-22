def vocales():
    print("Ingrese la palabra de la cual desea verificar las vocales")
    palabra = str(input("Palabra: "))
    palabra = palabra.lower()
    cantidad = palabra.count("a") + palabra.count("e") + palabra.count("i") + palabra.count("o") + palabra.count("u")
    print("Su palabra tiene", cantidad, "vocales")
    return cantidad
def palindromo (): 
    print("Ingrese la palabra que desea verificar si es palindromo")
    palindromo = str(input("Palabra:"))
    palindromo = palindromo.lower()
    if palindromo[::-1] == palindromo: 
        print("La palabra es un palindromo")
    else:
        print("La palabra no es un palindromo")
    return palindromo
    
def esvocal():
    print("Ingrese el caracter que desea verificar si es vocal o no")
    vocal = str(input("Letra: "))
    vocal = vocal.lower()
    if vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u": 
        print("El caracter es una vocal")
    else: 
        print("El caracter no es una vocal")
def suprime():
    print("Ingrese la palabra de la cual desea eliminar las vocales")
    a = str(input("Palabra: "))
    a = a.lower()
    a = a.replace("a", "")
    a = a.replace("e", "")
    a = a.replace("i", "")
    a = a.replace("o", "")
    a = a.replace("u", "")
    print("Su palabra sin vocales es la siguiente: ", a)


print("Este programa tiene varias funciones de uso para su preferencia")
print("Elija la opcion que desea ejecutar:")
print("1. Saber cuantas vocales tiene una palabra")
print("2. Saber si una es un palindromo")
print("3. Saber si un caracter ingresado es o no una vocal")
print("4. Eliminar las voales de una palabra\n")
print("Ingrese el numero de la opcion que desea ejecutar para ir a la funcion")

while True: 
    try: 
        opcion = int(input("Opcion:"))
        if opcion == 1: 
            vocales()
            break
        elif opcion == 2: 
            palindromo()
            break
        elif opcion == 3: 
            esvocal()
            break  
        elif opcion == 4: 
            suprime()
            break
        elif opcion > 4: 
            print("Ese valor no esta disponible")
            print("Por favor intenta otro")
    except: 
        print("Esa valor no esta disponible")
        print("Por favor intentalo de nuevo")