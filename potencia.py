print("calcula las potencias de 2")
base=2
exponentes=int(input("digite el numero al que le quiere sacar el exponente: "))

def generar_potencia(base,exponente): # el que genera la base  y exponente
    resultado=1
    for i in range(exponentes): # rango
        resultado *= base
    return resultado

print(generar_potencia(base,exponentes))
