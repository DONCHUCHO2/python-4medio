#la suma empieza en 0 para poder acumular los valores que se vallan ingresando
suma = 0
#estos son las variables que el usuario ingresara
n1 = int(input("ingrese un numero"))
n2 = int(input("imngrese otro numero"))
#se suman las dos variables ingresadas
suma = (n1 + n2)
#creamos un bucle donde si la variable suma es menor a 100 nos preguntara otro numero
while suma < 100:
    n2 = int(input("imngrese otro numero"))
#los datos se acumulan en la variable suma
    suma +=n2
    resultado = print("es igual a:",suma)

#al no cumplirse la condicion del ciclo el programna directamente pasa a finalizar
else:
    print("fin del programa")