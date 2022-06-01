"""""
hacer un progtrma queb muestre todos los numeros entre dos rangos que digite el usuario,
validar cual es mayor y cual es menor 
"""""
from itertools import count


rango1=int(input("Digite el inicio: "))
rango2=int(input("Digite el final: "))
if rango1 > rango2:
    print("El numero mayor es: ",rango1)
    print("El numero menos es:",rango2)
if rango1 < rango2:
    print("El numero mayor es: ",rango2)
    print("El numero menos es:",rango1)