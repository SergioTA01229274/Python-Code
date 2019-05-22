print("Este programa calcula la distancia entre dos puntos en un plano bidimencional ")
print("Por favor inserte las cordenadas del primer punto")

x1 = int(input("x1: "))
y1 = int(input("y1: "))

print("Ahora inserte las cordenadas del segundo punto")

x2 = int(input("x2: "))
y2 = int(input("y2: "))

distance = ((x2 - x1)**2) + ((y2 - y1)**2)

print("La magnitud de la distancia entre los puntos es de: ", distance, "unidades")
