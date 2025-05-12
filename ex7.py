senha="1234"

while True:
    tempSenha=input("Digite a senha: ")
    if tempSenha==senha:
        print("Acesso autorizado")
        break
    else:
        print("Acesso negado!!!")
        print("Tente novamente\n")