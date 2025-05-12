numeros=[""]*5
soma=0

for i in range(len(numeros)):
    numeros[i]=float(input(f"Digite o {i+1}º número: ").replace(',','.'))
    soma+=numeros[i]

media = soma / len(numeros)

print(f"A média dos números inseridos é: {media:.2f}")