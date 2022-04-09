notas=int(input("notas de los estidiantes: "))
vec=[]
n=0

for i in range(1,notas+1):
    nota=int(input("nota: "))
    n=n+nota
    vec.append(nota)