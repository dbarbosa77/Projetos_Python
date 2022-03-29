import random


aluno1 = input("Primeiro aluno: ")
aluno2 = input("Segundo aluno: ")
aluno3 = input("Terceiro aluno: ")
aluno4 = input("Quarto aluno: ")
aluno5 = input("Quinto aluno: ")


lista=[]
lista.append(aluno1)
lista.append(aluno2)
lista.append(aluno3)
lista.append(aluno4)
lista.append(aluno5)


sortear= random.randint(0,4)


print(f"O aluno escolhido foi {lista[sortear]}")

