import math 
print("Este programa calcula la circunferencia de una elipse\n")
print ("Para eso es necesario que introduzca el radio menor y el radio mayor\n")
print("Introduzca el radio mayor\n")

a = int(input("a:"))
print("Ahora introduzca el radio menor")
b = int(input("b:"))

perimeter = (2*math.pi)*(math.sqrt((a**2 + b**2)/2))       #formula para sacar la circunferencia de una elipse 

print("La circunferencia de la elipse segun los datos insertados es:\n ", "Circunferencia = ", perimeter, "cm")