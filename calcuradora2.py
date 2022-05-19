print("¿que opcion elijes?")
print("1 = suma")
print("2 = resta")
print("3 = multiplicacion")
print("4 = promedio")
print("5 = salir")
opcion = int(input("ingrese la opcion:"))


if opcion == 1:
    print("ingreso a la suma")
    n1= int(input("ingrese el valor 1: "))
    n2 = int(input("ingrese el valor 2: "))
    suma= n1+n2
    print(f"el resultado es {suma}")
elif opcion == 2:
    print("ingreso a la resta")

elif opcion == 3:
    print("ingreso a la multiplicacion")

elif opcion == 4:
    print("ingreso al promedio")

elif opcion == 5:
    print("hasta luego!")

else:
    print("ingrese una opcion")



