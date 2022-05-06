lista=[]
for x in range (5):
    valor=int(input("Ingrese un valor entero: "))
    lista.append(valor)
    if lista[x]<0:
        print("No se aceptan numeros negativos.")
        lista[x]=int(input("Por favor digite un numero positivo: "))
print(lista)
