#Fórmula del Interés Compuesto
invertir=int(input("Cantidad a invertir: "))
interes=float(input("Porcentaje del interés anual: "))
años=int(input("Número de años: "))
años=años/100
IC=invertir*(1+interes)**años
print("Sus ganancias serán de: ",IC)