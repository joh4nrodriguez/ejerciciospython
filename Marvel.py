puede_volar = input("¿puede volar?")
es_humano = input("¿Es humano?")
tiene_mascara = input("¿Tiene mascara?")

if puede_volar =='si':
    if es_humano =='si':
        if tiene_mascara =='si':
            print('Iroman')
        else:
            print('Capitan Marvel')
    else:
        if tiene_mascara =='si':
            print('Ronan Accuser')
        else:
            print('vision')
else:
    if es_humano == 'si':
        if tiene_mascara =='si':
            print('Spiderman')
        else:
            print('Hulk')
    else:
        if tiene_mascara =='si':
            print('Black Bolt')
        else:
            print('Thanos')               