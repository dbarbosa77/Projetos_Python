import string
import time
import random


a1=input("Digite o nome do aluno um: ")
a2=input("Digite o nome do aluno dois: ")
a3=input("Digite o nome do aluno três: ")
a4=input("Digite o nome do aluno quatro: ")

lista=[]
lista.append(a1)
lista.append(a2)
lista.append(a3)
lista.append(a4)


time.sleep(1.0)
print('sorteando...')
time.sleep(2.5)
random.shuffle(lista)
print("A ordem sorteada foi: ")
time.sleep(1.0)
contador = 0
apresentador = 1

for item in lista:
    if contador < 4:
        print(f"{lista[contador]} {apresentador}")
        contador += 1
        apresentador +=1
    time.sleep(1.0)  
    
       


