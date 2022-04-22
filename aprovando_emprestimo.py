casa= float(input("Qual o valor da casa? "))
salario = float(input("Qual o seu salário? "))
anos= int(input("Em quanto anos você pretende paga-lá? "))
mensal = casa/(anos*12)
trinta = salario * 30 / 100
print(mensal)

if mensal > trinta:
    print("O empréstimo foi negado.")
else:
    print("O seu empréstimo foi autorizado.")
