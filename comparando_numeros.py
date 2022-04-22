n = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

if n > n2:
    print(f"O valor {n} é MAIOR que o valor {n2}.")
elif n < n2:
    print(f"O valor {n} é MENOR que o valor {n2}.")
else:
    print(f"O valor {n} é IGUAL ao valor {n2}.")