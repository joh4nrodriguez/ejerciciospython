dri=input('Introduzca su identificacion:')
nif="TRWAGMYFPDXBNJZSQVHLCKE"
digitos= nif [int(dri)%23]
completo=dri+digitos
print(f'{completo}')
