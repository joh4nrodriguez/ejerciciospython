print("La suma de los números pares menores o iguales a ")
i = int(input("ingrese el numero inicial ="))
f = int(input("ingrese el numero final ="))
suma = 0
print("**los numeros pares del rango**")
while i <= f:
    if i % 2 == 0: # Listas 
        print(i)
    i+=1
    suma=suma+1
print("la suma de los numeros es:", suma)