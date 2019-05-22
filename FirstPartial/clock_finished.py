print("Escriba un numero de segundos\n ")

seconds = int (input("sec: "))
days = seconds//86400
z = seconds%86400   #residuo de segundos que sobran al tomar los necesarios para formar un dia 
hours = z//3600
z = seconds%3600         #residuo de segundos que sobran despues de tomar los necesarios para formar una hora 
minutes = z//60 
z = seconds%60     #residuo de segundos que sobran despues de formar un minuto 
seconds = z #residuo total de segundos que son insuficientes para formar algo mas 

print ("Su numero de segundos equivale a:\n ", days, "dias\n", hours, "horas\n", minutes, "minutos\n", " y", seconds, "segundos")


