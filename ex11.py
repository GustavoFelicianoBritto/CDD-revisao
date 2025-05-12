numeros=[""]*5
cont=0
for i in range(len(numeros)):
    numeros[i]=int(input("Digite o valor: "))
    if numeros[i]>50:
        cont+=1

print(f"{cont} numeros foram maiores que 50")