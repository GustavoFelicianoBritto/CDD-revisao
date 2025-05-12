numeros=[""]*5
soma=0

for i in range(len(numeros)):
    numeros[i]=float(input(f"Digite o {i+1}º número: ").replace(',','.'))
    soma+=numeros[i]

media = soma / len(numeros)

if media>=7:
    print("Aprovado")
elif media>=4:
    print("Recuperação")
elif media >=0:
    print("Reprovado")
else:
    print("Média inválida")
