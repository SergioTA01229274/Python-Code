import math
print("Ingrese un numero que representara el radio de una esfera en cm \n ")

radius = int(input("radius = "))

Volume = ((4)*math.pi*((radius)**3))/3    #formula para obtener el volumen de una esfera
Area = (4)*math.pi*((radius)**2)

print("Con respecto al radio otorgado, la esfera tiene un volumen de:\n ", "V = ", Volume, "cm cubicos\n ", "Y un area de:\n ", "Area = ", Area, "cm cuadrados")
