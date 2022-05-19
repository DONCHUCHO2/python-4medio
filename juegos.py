edad = int(input("ingresa tu edad"))

if edad < 4 :
    print("entrada gratis")
elif edad >= 4 and edad <= 17:
    print("debe pagar 5$")
elif edad >= 18:
    print("debes pagar 10$")
else:
    print("Elección no valida")