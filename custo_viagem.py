distancia = float(input("Qual a distância da sua viagem?  "))

if distancia <= 200:
    valor = distancia * 0.50
    print(f"O valor da sua passagem será de R${valor:.2f}")
else:
    valor = distancia *0.45
    print(f"O valor da sua passagem será de R${valor:.2f}")
    
