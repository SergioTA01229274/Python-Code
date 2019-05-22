num = input("Introduce un numero de 7 digitos: ")

L = list()

for i in num:
    L.append(i)

x = 0
for i in L:
    x += int(i)

if x == 25:
    print("Los digitos del numero suman 25")
else:
    print("Los digitos del numero no suman 25")
