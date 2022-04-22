from datetime import date

print("""[ 1 ] HOMEM
[ 2 ] MULHER""")

sexo = int(input("Qual é o seu sexo: "))
              



if sexo == 1:
    nasc = int(input("Ano de nascimento: "))
    atual = (date.today().year)
    print(f"Quem nasceu em {nasc} tem ou fará {atual- nasc} anos em {atual}")


    if atual - nasc == 18:
        print("Seu alistamento será esse ano.")
    elif atual - nasc < 18:
        print(f"Ainda faltam { (nasc + 18) - atual}  anos para o alistamento")
        print(f"Seu alistamento será em {atual - (atual - nasc - 18) }")
    else:
        print("Você tem mais de 18 anos.")
        print(f"Seu alistamento foi a {(atual - nasc - 18)} anos atrás.")
        print(f"No ano de {atual - (atual - nasc - 18) } ")
        
elif sexo == 2:
    print("Você não precisa se alistar.")
        
else:
    print("Digite uma opção válida entre 1 e 2.")