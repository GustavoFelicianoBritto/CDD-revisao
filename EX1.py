nomes=[""]*5
nameWithA=[]

for i in range(len(nomes)):
    nomes[i]=input(f"Digite o {i+1}º nome: ").lower()
    tempname=nomes[i]
    if tempname[0]=="a":
        nameWithA.append(tempname)

print("Palavras iniciadas com A: ")
for i in range(len(nameWithA)):
    print(nameWithA[i], end=", ") if i< len(nameWithA)-1 else print(nameWithA[i])


