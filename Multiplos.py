
valorn=int(input("digite su numero para sacar el multiplo: "))
valorm=int(input("digite su numero para la cantidad a sacar del multiplo: "))

def generar_multiplo(valorn,valorm): # genera los multiplos del número escrito por el usuario
    return [valorn * i for i in range(1,valorm + 1)]
print(generar_multiplo(valorn,valorm))