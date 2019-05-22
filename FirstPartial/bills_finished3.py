print("Escriba un monto de dinero\n ")

pesos = int(input("Pesos: "))
bills1 = pesos//1000 
z = pesos%1000 
print(bills1, "billetes de 1000\n ")

bils2 = z//500    
a = pesos%500  
print(bils2, "billetes de 500\n ")

bils3 = a//200       
b = pesos%200
print(bils3, "billetes de 200\n ")

bils4 = b//100         
c = pesos%100
print(bils4, "billetes de 100\n ")

bils5 = c//50             
d = pesos%50 
print(bils5, "billetes de 50\n ")

bils6 = d//20            
e  = pesos%20
print(bils6, "billetes de 20\n ")

coins1 = e//10       
f = pesos%10  
print(coins1, "monedas de 10\n ")

coins2 = f//5        
g = pesos%5 
print(coins2, "monedas de 5\n ")

coins3 = g//2       
h = pesos%2    
print(coins3, "monedas de 2\n ")

pesos2 = h
print(pesos2, "monedas de 1")