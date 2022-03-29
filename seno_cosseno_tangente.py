from cmath import acos, asin, atan, cos, sin, tan
import math

angulo = int(input("Digite o angulo que você deseja: "))

print(f"O seno de {angulo} é {math.sin(math.radians(angulo)):.2f}")
print(f"O cosseno de {angulo} é {math.cos(math.radians(angulo)):.2f}")
print(f"A tangente de {angulo} é {math.tan(math.radians(angulo)):.2f}")
