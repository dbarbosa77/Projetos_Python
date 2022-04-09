import random
import time
print("-=-"*30)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-"*30)
lista=[1,2,3,4,5]
escolhido= random.choice(lista)


numero=int(input("Digite o número que você acha que eu pensei: "))
print('PROCESSANDO...')
time.sleep(1.5)

if escolhido == numero:
    print(f"Uau, você acertou, eu pensei no número {escolhido}")
else:
    print(f"Você errou, eu pensei no número {escolhido}")