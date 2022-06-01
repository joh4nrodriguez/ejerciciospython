produccion= dict(
    Enero=35627,
    febrero=567483,
    marzo=64738,
    abril=6547382,
    mayo=564738,
    junio=637282,
    julio=46778,
    agosto=6929,
    septiembre=89234,
    octubre=67292,
    noviembre=81239,
    diciembre=89,
)
llave_min=min(produccion.keys(), key=lambda k:produccion[k])
print('El mes de menor produccion fue:',llave_min,produccion[llave_min])

llave_max=max(produccion.keys(), key=lambda k:produccion[k])
print('El mes de mayor produccion fue:',llave_max,produccion[llave_max])

prom=tuple(produccion.values())
b=len(prom)
suma=0
for valor in prom:
    suma+=valor
print('El promedio es:',suma/b)

for key in produccion.keys():
    if(produccion[key]>=prom):
        
     print('el mes',(key),'es mayor que el promedio')
    
    elif (produccion[key]<=prom):
        print(f'el mes:', {key}, 'es menor que el promedio')
