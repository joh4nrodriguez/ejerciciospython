ciudades=dict(
    Ibague=501991,
    Barranquilla=1273646,
    Cali=2205680,
    Bogota=7715778,
    Neiva=340512,
)    
#for ciudades in ciudades.keys():   Mostar las claves
#for ciudades in ciudades.values(): #Mostrar los valores de las claves
for clave, valor in ciudades.items():# separa los valores de las claves
 print(f'{clave}:{valor}')  
       
