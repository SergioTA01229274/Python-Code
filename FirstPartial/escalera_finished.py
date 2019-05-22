import math 

print("Este programa calcula el largo necesario de una escalera para alcanzar una altura especifica")
print("Inserte la altura que se queire alcanzar")

high = float(input("Altura: "))
print("Ahora inserte el angulo al que piensa poner la escalera")
angle = float(input("Angulo: "))

c = math.radians(angle)

Long = high/math.sin(c)

print("El largo necesario es: ", Long, "Metros")
