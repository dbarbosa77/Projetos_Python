nome=input("Nós vamos calcular sua média, mas primeiro, como você prefere ser chamado(a)? ")
RA=input(f"Olá {nome}, qual o seu RA? ")
print(f"{nome}, de RA:{RA} ")
n1=float(input(f"{nome}, Qual foi a sua primeira nota? "))

while n1<0 or n1>10:
        print("Sua nota não é válida, coloque um número de 0 até 10")
        n1=float(input(f"{nome}, Qual foi a sua primeira nota? "))
        n1= round(n1,2)

print(f"A nota da sua primeira prova é {round(n1,2)}")


n2=float(input(f"{nome}, Qual foi a sua segunda nota? "))

while n2<0 or n2>10:
        print("Sua nota não é válida, coloque um número de 0 até 10")
        n2=float(input(f"{nome}, Qual foi a sua segunda nota? "))
        n2=round(n2,2)

print(f"A nota da sua segunda prova é {round(n2,2)}")


n3=float(input(f"{nome}, Qual foi a sua terceira nota? "))

while n3<0 or n3>10:
        print("Sua nota não é válida, coloque um número de 0 até 10")
        n3=float(input(f"{nome}, Qual foi a sua terceira nota? "))
        n3=round(n3,2)

print(f"A nota da sua terceira prova é {round(n3,2)}")


media= (n1+n2+n3) /3
print(f'A média do {nome} é: {round(media,2)}')

if media < 7:
    print(f"Você está abaixo da média: {round(media,2)}")

elif media > 7:
    print(f"Parabéns, você está acima da média: {round(media,2)}")

elif media==7:
    print(f"Você está na média: {round(media,2)}")

else:
    print("Algo está errado com sua nota")