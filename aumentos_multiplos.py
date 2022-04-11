salario1= int(input("Qual o seu salário: "))


if salario1 > 1250:
    aumento = (salario1 * 10) / 100
    de= 10
else:
    aumento = (salario1*15) / 100
    de=15

salario = salario1 + aumento

print(f"Se você antes recebia R${salario1:.2f} agora passa a receber R${salario:.2f} agora, pois houve um aumento de {de}%")