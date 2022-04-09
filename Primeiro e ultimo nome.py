from tkinter import N


n= str(input("Qual o seu nome completo? ")).strip()
n = n.title()
nome=n.split()
print(f"Seu primeiro nome é {nome[0]} e seu ultimo nome é {nome[len(nome)-1]}"  )
