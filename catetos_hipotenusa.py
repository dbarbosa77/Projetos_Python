oposto = float(input("Comprimento do cateto oposto: "))
adjacente = float(input("Comprimento do cateto adjacente: "))

hipotenusa = (oposto**2 + adjacente**2) **(1/2)
print(f'a hipotenusa vai medir: {hipotenusa:.2f}')