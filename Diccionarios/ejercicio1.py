lista1=[]
lista2=[]

for usuario in range(6):
    usuario=int(input("Digite 20 elemtos: "))
    if usuario%2==0:
        lista1.append(usuario)
    else:
        lista2.append(usuario)
print(lista1)
print(lista2)