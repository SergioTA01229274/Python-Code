
print("este programa hacce una suma de una serie de numeros consecutivos")
print("Ingrese el primer numero de la serie")

a = int(input("a: "))
print("ingrese la diferencia que va a haber entre cada numero")

d = int(input("d: "))
print("Ingrese cuantos numeros quiere sumar")
n = int(input("n: "))

suma = (n/2)*((2*a) + (n - 1)*(d))

print("El resultado de la sumatoria es: ")
print(suma)