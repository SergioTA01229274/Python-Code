import random
import os


def tirada(n):
    cont = 1
    result = 0
    while cont < n + 1:
        number = random.randint(1, 6)
        print("Tiro", cont, ":", number, "puntos")
        cont += 1
        result += number
    return result


def desordenaPalabra(msg):
    word = msg
    word = word.replace(" ", "")
    newWord = []
    result = ""
    '''for i in word:
        newWord.append(i)'''
    newWord = list(word)
    for j in range(len(newWord)):
        character = random.choice(newWord)
        result += character
        newWord.remove(character)
    return result


def menu():
    print("Este programa puede realizar dos tipos de tareas diferentes")
    print("1. Obtener la suma de puntos obtenidos por tirar n veces un dado")
    print("2. Revolver una palabra\n")
    print("Si desea terminar el programa teclee 3")


condition = True

menu()
while condition:
    option = input("numero de opcion:")
    try:
        option = int(option)
        if option == 1:
            os.system("cls")
            print("Ingrese cuantas veces desea lanzar el dado")
            b = True
            while b:
                a = input("n: ")
                try:
                    a = int(a)
                    print(tirada(a))
                    print("¿Desea vovler al menu iniical?")
                    c = input("Respuesta: ")
                    c = c.lower()
                    if c == "si":
                        os.system("cls")
                        menu()
                        break
                except ValueError:
                    print("Debe ingresar un numero, intentelo de nuevo")
        elif option == 2:
            os.system("cls")
            print("Ingrese la palabra que desea revolver")
            a = input("palabra: ")
            print(desordenaPalabra(a))
            print("¿Desea vovler al menu iniical?")
            c = input("Respuesta: ")
            c = c.lower()
            if c == "si":
                os.system("cls")
                menu()
        elif option == 3:
            print("bye")
            break
    except ValueError:
        print("Debe ingresar un numero, por favor intentelo de nuevo")
