#Crear funcion
def suma(a,b):
    c=a+b
    print(f"El resultado de la suma es:{c}")
#Programa principal
a=int(input("Digite un valor: "))
b=int(input("Digite otro valor: "))
#Llamar a la funcion
suma(a,b)

def suma1(a,b):
    c=a+b
    return c
#Programa principal
a=int(input("Digite un valor: "))
b=int(input("Digite otro valor: "))
c=suma1(a,b)
#print(f"El resultado de la suma es:{c}")
print(f"El resultado de la suma es:{suma1(a,b)}")