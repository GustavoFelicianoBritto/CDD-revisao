frase = input("Digite a frase a ser analisada: ").lower()
cont=0
for i in frase:
    if i=="a":
        cont+=1

print(f"Na frase\n{frase}\nA letra A apareceu {cont} vezes")
