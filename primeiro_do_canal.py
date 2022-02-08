nome="douglas" #string
idade=21 #int
nota=8.9 #float
aprovado=True #bool
nome=input("Qual o seu nome? ")
n1=int(input(f'Olá {nome}, digite um número '))
n2=int(input(f'{nome}, digite mais um número '))
operacao=input("Digite uma operação (+,-,/,*) ")
if operacao =="+":
    resultado=n1+n2
    operacaonome="soma"
elif operacao =="-":
    resultado=n1-n2
    operacaonome="subtração"
elif operacao =="/":
    resultado=n1/n2
    operacaonome="divisão"
elif operacao =="*":
    resultado=n1*n2
    operacaonome="multiplicação"
else:
    print("se fudeu ein porra")
    resultado=0
    operacaonome="erro"

if operacaonome !="erro":
    print(f"A {operacaonome} de {n1} com {n2} é igual a {resultado}, entendeu {nome}, porra? ")
