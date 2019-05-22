import math 

def multiplo(N1,N2):
    if N1%N2 == 0: 
        print("El numero x: ", N1, ",es divisible por el numero y: ", N2)
    else: 
        print("El numero x: ", N1, ",no es divisible por el numero y: ", N2)
    return N1%N2        
def volumen(radio):
    Volume = ((4)*math.pi*(radio**3))/3    #formula para obtener el volumen de una esfera 
    Area = (4)*math.pi*(radio**2)
    print("Con respecto al radio otorgado, la esfera tiene un volumen de\n ", "V = ", Volume, "cm cubicos\n ", "Y un area de\n ", "Area = ", Area, "cm cuadrados")
    return Volume 
    return Area

def segundos(sec):
    days = sec//86400
    z = sec%86400   #residuo de segundos que sobran al tomar los necesarios para formar un dia 
    hours = z//3600
    z = sec%3600         #residuo de segundos que sobran despues de tomar los necesarios para formar una hora 
    minutes = z//60 
    z = sec%60     #residuo de segundos que sobran despues de formar un minuto 
    sec = z #residuo total de segundos que son insuficientes para formar algo mas 
    print ("Su numero de segundos equivale a:\n ", days, "dias\n", hours, "horas\n", minutes, "minutos\n", " y", sec, "segundos")
    return minutes
    return hours
    return days
def convertidor(pies,medida):
    yards = pies/3 
    inches = pies*12
    cm = inches*2.54
    meters = cm/100
    
    if medida == "yardas": 
        print("El numero de", pies,"pies",  "equivale a ", yards, "yardas")
    elif medida == "pulgadas": 
        print("El numero de", pies, "pies equivale a ", inches, "pulgadas")
    elif medida == "metros": 
        print("El numero de", pies, "pies equivale a ", meters, "metros")
    elif medida == "centimetros":
        print("El numero de", pies, "pies equivale a ", cm, "centimetros")
    return meters
    return cm 
    return yards 
    return inches 
def comparador(numero1, numero2):
    
    if numero1 < numero2: 
        print("-1")
        return -1 
    elif numero1 == numero2: 
        print("0")
        return 0 
    elif numero1 > numero2: 
        print("1")
        return 1 
        
print("Este es un programa funciona como un menu de diferentes funciones que se pueden ejecutar")
print("Las opciones a ejecutar son:\n",  "1. Calcular si un numero es divisible por otro\n", "2. Calccular el volumen de una esfera\n", "3. Calcular a cuanto equivale un numero determinado de segundos\n", "4. Convertidor de pies a otra unidad de medicion\n", "5. Comparar si un numero es mayor que otro")

print("Ingrese la opcion que decea ejecutar: Divisible, Esfera, Segundos, Convertidor, Comparador")

opcion = str(input("Eleccion: "))

if opcion == "Divisible": 
    print("Esta funcion verifica si un numero es divisible por otro")
    print("Ingrese un numero")
    n1 = int(input("x: "))
    print("Inserte otro numero")
    n2 = int(input("y: "))
    multiplo(n1,n2)
elif opcion == "Esfera": 
    print("Esta funcion calula el volumen y el area superficial de una esfera")
    print("Ingrese la magnitud del radio de dicha esfera a calcular")
    r = int(input("Radio:"))
    volumen(r)
elif opcion == "Segundos":
    print("Este programa calcula la equivalencia de segundos en minutos, horas y dias")
    print("Ingrese un numero de segundos")
    seconds = int(input("Segundos: "))
    segundos(seconds)
elif opcion == "Convertidor": 
    print("Este programa calcula la equivalencia de un numero de pies a otras unidades de medicion")
    print("Ingrese un numero de pies a calcular")
    unit_foots = int(input("Pies: "))
    print("Ahora ingrese la unidad de medicion que decea obtener")
    unit = str(input("Unidad:"))
    convertidor(unit_foots,unit)
elif opcion == "Comparador": 
    print("Esta funcion compara si un numero me mayor que otro")
    print("Para eso es necesario que ingrese dos numeros")
    
    print("Ingrese el primer numero")
    num1 = int(input("Numero 1: "))
    print("ingrese el segundo numero")
    num2 = int(input("Numero 2: "))
    
    comparador(num1,num2)