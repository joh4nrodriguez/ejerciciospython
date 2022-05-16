lista=[]
for x in range(1,6):
    valor=int(input("Ingrese los numeros de la lista: "))
    lista.append(valor)
    
while valor <0:
    print("¡Ha escrito un número negativo! Inténtelo de nuevo")
    lista.remove(valor)
    valor = int(input("Escriba un número positivo: "))
print(lista)
