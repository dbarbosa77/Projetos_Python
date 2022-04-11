a=float(input("Qual o comprimento da primeira reta: "))
b=float(input("Qual o comprimento da segunda reta: "))
c=float(input("Qual o comprimento da terceira reta: "))

if a < b+c and b < a + c and c < a + b:
    print("É possível formar um triângulo com esses comprimentos.")
else:
    print("Não é possível formar um triângulo com esses comprimentos.")