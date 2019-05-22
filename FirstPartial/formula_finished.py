import math 

print("Este programa calcula las soluciones a una ecuacion cuadratica por medio de la formula general")
print("Para eso es necesario que inserte los coeficientes de la ecuacion")

print("Inserte el primer coeficiente")
a = int(input("a: "))

print("Inserte el segundo coeficiente")
b = int(input("b: "))

print("Inserte el tercer coeficiente")
c = int(input("c: "))

if a == 0: 
    if b == 0: 
        print("Los valos otorgados no perteneceen a una funcion")
        print("Esos valores representan una constante")
    else: 
        x = -c/b 
        print("Los valosres otorgados pertenecen a una funcin lineal")
        print("La solucion es:\n ", "x = ", x)
else: 
    d = (b**2) - 4*a*c
    e = ((-b)/(2*a))
    i = complex((math.sqrt(-(d)))//(2*a))
    if d >= 0: 
        x1 = ((-b) + math.sqrt(d))/(2*a)
        x2 = ((-b) - math.sqrt(d))/(2*a)
        print("La solucion de la ecuacion en base a los valores dados es:\n ", x1, "= x1\n", x2, "= x2")   #el algoritmo funciona hasta aqui 
    elif d < 0:  
        x3 = e + i 
        x4 = e - i 
        print("Los valores otorgados indican un discriminante negativo, por lo que una solucion para numeros imaginarios es necesaria")
        print("La solucion en base a los valores dados seria:\n", x3, "= x1\n", x4, "= x2") 
        