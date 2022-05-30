#este tipo de lista es inmutable(no se puede modificar)
par = (1,2)
lista = [1,2]

print(par)
print(lista)

lista[0] = 5
#el tuple no se puede modificar
par[0] = 5

print(par[0])
print(lista[0])
