sexo = input("¿cual es tu sexo?")
sala = input("dime tu grupo {A o B}: ")
if sexo == "f" and sala=="A":
    print("bienvenido a la sala A")
elif sexo == "m" and sala == "A":
    print("no puedes entrar por que perteneces al grupo B")
elif sexo == "m" and sala == "B":
    print("bienvenido a la sala B")
else:
    print("ELECCION NO VALIDA")


