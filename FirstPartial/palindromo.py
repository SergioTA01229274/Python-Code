print("Este programa verifica si una palabra o una frase es un palindromo")
print("Por favor inserte una palabra o frase")

palabra = str(input("Palabra: "))

if palabra.count(" ")  >= 1: 
    palabraModificada = palabra.replace(" ", "")
    if palabraModificada == palabraModificada[::-1]: 
        print("La palabra es un palindromo")
    else: 
        print("La palabra no es un palindromo")