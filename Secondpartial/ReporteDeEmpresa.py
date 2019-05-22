import os
import datetime


def IngresarDatos(numLin1, c):
    Doc = open("Production Report.txt", 'a')
    Doc.write("\n")
    today = datetime.date.today()
    for i in range(numLin1):
        tomorrow = today + datetime.timedelta(days=c)
        LineNumber = input("Numero de linea: ")
        Doc.write("Linea " + LineNumber)
        Doc.write(",")
        Turn = input("Turno: ")
        Doc.write("Turno " + Turn)
        Doc.write(",")
        date = tomorrow
        Doc.write(str(date))
        Doc.write(",")
        TotalProducts = input("Total de productos de la semana: ")
        Doc.write(TotalProducts)
        Doc.write(",")
        Stop = input("Veces que se detuvo la linea: ")
        Doc.write(Stop)
        os.system("cls")


def Resumen(NumLin, NumT):
    Resumen = open("Resumen.txt", 'w')
    try:
        Doc = open("Production Report.txt", 'r')
    except ValueError:
        print("No se puede abrir el archivo")
    for LineData in Doc:
        Data = LineData.split(",")
        if Data[0] == NumLin and Data[1] == NumT:
            Resumen.write("Numero de linea: " + Data[0])
            Resumen.write("\n")
            Resumen.write("Turno: " + Data[1])
            Resumen.write("\n")
            Resumen.write("Total de productos a la semana: " + Data[3])
            Resumen.write("\n")
            Resumen.write("Veces que se detuvo la linea: " + Data[4])
            Resumen.write("\n")
            D = Data[2]
            D = D.split("-")
            Day = datetime.date(int(D[0]), int(D[1]), int(D[2]))
            y = Day.weekday()
            if y == 1:
                x = "Martes"
                Resumen.write("Día en que más veces se detuvo la línea: " + x)
                Resumen.write("\n")
            elif y == 2:
                x = "Miercoles"
                Resumen.write("Día en que más veces se detuvo la línea: " + x)
                Resumen.write("\n")
            elif y == 3:
                x = "Jueves"
                Resumen.write("Día en que más veces se detuvo la línea: " + x)
                Resumen.write("\n")
            elif y == 4:
                x = "Viernes"
                Resumen.write("Día en que más veces se detuvo la línea: " + x)
                Resumen.write("\n")
            elif y == 5:
                x = "Sabado"
                Resumen.write("Día en que más veces se detuvo la línea: " + x)
                Resumen.write("\n")
            elif y == 6:
                x = "Domingo"
                Resumen.write("Día en que más veces se detuvo la línea: " + x)
                Resumen.write("\n")
            elif y == 7:
                x = "Lunes"
                Resumen.write("Día en que más veces se detuvo la línea: " + x)
                Resumen.write("\n")
            Resumen.write("\n")     # sumar productos de la linea a lo largo d ela semana y evaluar el numero de veces mas alto en el que se detuvo la linea.


def ReiniciarSemana():
    Doc = open("Production Report.txt", 'w')
    today = datetime.date.today()
    begin = today.day
    end = today + datetime.timedelta(days=7)
    Doc.write("Semana del " + str(begin) + " al " + str(end.day) + " de Nov:")


def ConsultasParciales(NumLin, NumT):
    try:
        Doc = open("Production Report.txt", 'r')
    except ValueError:
        print("No se puede abrir el archivo")
    a = ""
    for LineData in Doc:
        Data = LineData.split(",")
        if Data[0] == NumLin and Data[1] == NumT:
            a = LineData
    return a


def menu():
    print("Bienvenido al software de control y registro de datos de XETU")
    print("Este software puede llevar a cabo varias tareas")
    print("1. Ingresar datos de la linea de produccion al documento de registro.")
    print("2. Generar un documento de resumen de una linea en especifico.")
    print("3. Llevar a cabo una consulta parcial de una linea en especifico.")
    print("4. Reiniciar la semana en el documento de registro.")
    print("5. Salir.\n")


def w():
    return "Aun no se generan datos o de la linea o del turno en cuestion."


menu()
while True:
    opcion = int(input("Ingrese el numero de la opcion que desea ejecutar: "))
    if opcion == 1:
        os.system("cls")
        Num = int(input("Ingrese el numero dias de los cuales ingresara datos: "))
        Num2 = int(input("Ingrese el numero de lineas sobre las cuales ingresara datos: "))
        os.system("cls")
        ReiniciarSemana()
        cont = 0
        for i in range(Num):
            IngresarDatos(Num2, cont)  # Esto es importante
            cont += 1
        answer = input("¿Desea regresar al menu?: ")
        if answer == "si":
            os.system("cls")
            menu()
        elif answer == "no":
            break
    elif opcion == 2:
        os.system("cls")
        num = input("Ingrese la linea sobre la cual desea el resumen: ")
        num2 = input("Ingrese el turno de la linea sobre el cual desea el resumen: ")
        d = open("Production Report.txt", 'r')
        t = d.read()
        text = t[0:]
        if num in text and num2 in text:
            os.system("cls")
            Resumen(num, num2)
            print("Se ha generado el resumen exitosamente")
            answer = input("¿Desea regresar al menu?: ")
            if answer == "si":
                os.system("cls")
                menu()
            elif answer == "no":
                break
        else:
            print("Aun no se han generado datos o de la linea o del turno en cuestion")
            answer = input("¿Desea regresar al menu?: ")
            if answer == "si":
                os.system("cls")
                menu()
            elif answer == "no":
                break
    elif opcion == 3:
        os.system("cls")
        num = input("Ingrese la linea sobre la cual desea la consulta parcial: ")
        num2 = input("Ingrese el turno de la linea sobre el cual desea la consulta: ")
        D = open("Production Report.txt", 'r')
        t = D.read()
        text = t[0:]
        if num in text and num2 in text:
            D.close()
            print("Esta es a informacion de la linea y turno en cuestion: ")
            print(ConsultasParciales(num, num2))
            answer = input("¿Desea regresar al menu?: ")
            if answer == "si":
                os.system("cls")
                menu()
            elif answer == "no":
                break
        else:
            print(w())
            answer = input("¿Desea regresar al menu?: ")
            if answer == "si":
                os.system("cls")
                menu()
            elif answer == "no":
                break
    elif opcion == 4:
        ReiniciarSemana()
        print("Se ha reiniciado el documento de registro de datos")
        answer = input("¿Desea regresar al menu?: ")
        if answer == "si":
            os.system("cls")
            menu()
        elif answer == "no":
            break
