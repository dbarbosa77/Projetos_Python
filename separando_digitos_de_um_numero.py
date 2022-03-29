import time

num=int(input("Informe um número: "))
print(f"Analisando o número {num}")
time.sleep(2.0)
print(f"Quantidade de casas: {len(str(num))}")
time.sleep(1.0)
print(f"Divisível por 10: {round(num/10)}")
time.sleep(4.0)
print(f"Divisível por 100: {round(num/100)}")
time.sleep(1.0)
print(f"Divisível por 1000: {round(num/1000)}")
time.sleep(2.0)


u= num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
dm = num // 10000 % 10
cm = num // 100000 % 10
print(f"Unidade: {u}")
print(f"Dezena: {d}")
print(f"Centena: {c}")
print(f"Unidade de milhar: {m}")
print(f"Dezena de milhar: {dm}")
print(f"Centena de milhar: {cm}")