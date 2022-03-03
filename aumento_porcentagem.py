salario=int(input("Qual o seu salário? "))
aumento=int(input('Qual foi a porcentagem do aumento?'))

def porcentagem(salario,aumento):
    return (salario*aumento/100)+salario


calculo = porcentagem(salario,aumento)

print(calculo)
