print("hucha")

objetivo = float(input("¿cuantos euros quiere ahorrar?"))

ahorrado = 0.0
while objetivo > ahorrado:
       ahorrado += float(input("¿cuantos euros quiere meter en la hucha?:"))
print(f"¡objetivo conseguido! ha ahorrado usted {ahorrado} euros")