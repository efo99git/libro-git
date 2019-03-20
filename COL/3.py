numero= int (input("Dame un número: "))
while numero <= 0:
    print ("Pon uno positivo")
    numero= int (input("Dame un número: "))
for i in range(numero):
    if i%2 != 0:
        print(i, end=", ")

