

from audioop import reverse

#Primera funcion
def mostrarCadena(cadena):
    for i in lista:
        print(i)
        cadena+=str(i)+coma
    return cadena

#Seguna funcion
def listaInversa(lista):
    lista.sort(reverse=True)
    lista2=lista
    return lista2

#Tercera funcion
def menu(lista):
    menu = int(input("seleccione \n 1. Para buscar en la lista \n 2. Para salir\n"))

    while menu> 2:
        print('digite un numero que este dentro del rango (1 o 2)')
        menu = int(input("seleccione \n 1. Para buscar en la lista \n 2. Para salir\n"))

    while menu == 1:
        letra = input("Introduzca la palabra a buscar en la lista: ")
        for i in lista:
            if i == letra:
                print('es igual ')
            else:
                print('no es igual')
        menu = int(input("selecione \n 1. Para buscar en la lista \n 2. Para salir\n"))

    if menu == 2:
        print('Te esperamos pronto')

#Cuarta funcion
def contar(lista):
    letra = input("Introduzca una de las palabras que estan dentro de la lista para contar sus silabas: ")
    for i in lista:
        if i == letra:
            verdad=len(i)
            print(f'{verdad}')
        else:
            print(f"NULL")

#Base
lista=['johan','steeven','ana','luisa','joan','daniel','adriany','alejandra','diego','juan']
cadena=""
coma=","

print("\n El programa mostrara en una variable la lista \n")

cadena =mostrarCadena(cadena)
print(f"{cadena}")

print("\n Se imprimira la lista en de manera desendente alfabeticamente \n")

lista2 =listaInversa(lista)
print(f"{lista2}")
# # La lista buscada quedara ordenada de forma descendente (Z,A)
print("\n El programa dira si ese nombre esta dentro de la lista \n")

menu(lista)

print("\n El programa contara todas las silabas \n")

contar(lista)

print("El programa ha finalizado")


 

