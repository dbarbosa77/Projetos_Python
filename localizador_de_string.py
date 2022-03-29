


nome = str(input("Qual o seu nome? ")).strip()
nome=nome.upper()

chegar =nome.find("SILVA")


silva= chegar + 5 

if nome[chegar:silva] == "SILVA":
    print("Seu nome tem Silva.")
else:
    print("Seu nome não tem Silva.")
