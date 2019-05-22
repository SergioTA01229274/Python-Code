print(" Escriba un numero de pies\n")

unit_foots = int(input("ft: "))
yards = unit_foots/3 
inches = unit_foots*12
cm = inches*2.54
meters = cm/100

print("Su numero de pies equivale a: \n", yards,"Yardas, ",inches, "pulgadas, ", cm, "Centimetros, ", meters, "metros "  )