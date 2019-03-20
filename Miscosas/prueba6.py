dinero=int(input("¿Cual es tu renta?: "))
if dinero<10000:
    print("Debes pagar",dinero *0.05,"euros, que tiene un tipo de impositivo del 5%")
elif 10000<=dinero<20000:
    print("Debes pagar",dinero *0.15,"euros, que tiene un tipo de impositivo del 15%")
elif 20000<=dinero<35000:
    print("Debes pagar",dinero *0.20,"euros, que tiene un tipo de impositivo del 20%")
elif 35000<=dinero<60000:
    print("Debes pagar",dinero *0.30,"euros, que tiene un tipo de impositivo del 30%")
else:
    print("Debes pagar",dinero *0.45,"euros, que tiene un tipo de impositivo del 45%")