import math # es la libreria para hacer cualquier operacion matematica

# ejercicio matematico while
"""
Ejercicio para sacar la raiz cuadrada a cualquier numero positivo,
si es negativo se le va a darla oportunidad al usuario de volver a digitar
el numero.
"""
print("Programa para sacar la raiz a un numero")
numero=int(input("Ingrese el numero a sacar la raiz: "))#variable donde se va a almacenar el numero que ingrese el usuario

while numero<0:# el numero debe de ser mayor a 0
    print("El numero debe de ser positivo")#si es menor a 0 me va a imprimir un mensaje#donde le dice al usuario que el numero debe de ser positivo
    numero=int(input("Ingrese el numero a sacar la raiz:"))#oportunidad de que el usuario vuelva a digitar el numero
print(f'La raiz de {numero} es: {(math.sqrt(numero))}')# me va a imprimir el numero que digito el usuario
#y el resultado de la raiz. la funcion math.sqrt es para calcular la raiz cuadrada a cualquier numero