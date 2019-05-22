def terremoto(magnitud):
    if magnitud < 3.5:
        print("Un terreomoto de esa escala generalmente no se siente, pero es registrado")
    elif 3.5 <= magnitud and magnitud <= 5.4: 
        print("Un terreomoto de esa escala puede sentirse pero solo causa bajas materiales menores")
    elif 5.5 <= magnitud and magnitud <= 6.0: 
        print("Un terreomoto de esa escala ocasiona bajas ligeras a edificios")
    elif 6.1 <= magnitud and magnitud <= 6.9: 
        print("Un terreomoto de esa escala ocasiona bajas materiales severas en areas muy pobladas")
    elif 7.0 <= magnitud and magnitud <= 7.9: 
        print("Un terreomoto de esa escala causa bajas materiales graves")
    elif magnitud >= 8.0: 
        print("Un terreomoto de esa escala causa destuccion total a comunidades cercanas")



print("Este programa evalua las bajas materiales que puede causar un terremoto de cierta escala")
print("Para eso es necesario que ingrese la magnitud del terremoto")
escala = float(input("Escala del terremoto en Richter: "))
terremoto(escala)
