numero= int(input("Dame un años: "))
can=float(input("Dame cantidad: "))
por=float(input("Dame porcentaje: "))
for i in range (numero):
    can +=can*por/100
    print (can)