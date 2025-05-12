import random

secretNumber= random.randint(1,100)

guess=None
tentativas=10

while guess!=secretNumber:

    guess = int(input("Advinhe um número de 1 a 100: "))
    tentativas+=1

    if guess==secretNumber:
        print(f"Parabéns, você acertou o número na {tentativas}ª tentativa")
    elif guess < secretNumber:
        print(f"Ainda não, o número secreto é maior que {guess}")
    else:
        print(f"Ainda não, o número secreto é menor que {guess}")