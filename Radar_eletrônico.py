from tracemalloc import stop


limite = 80
print(f"O limite da via é de {limite}Km/h")
velocidade= int(input("Qual é a velocidade atual do carro em Km/h? "))
multa = (velocidade - limite) * 7
multa = str(multa)



if velocidade > limite:
    print(f"MULTADO! Você excedeu o limite máximo permitido que é de {limite}Km/h \n Você deve pagar uma multa de R${multa + ',00'}")
else: 
    pass

print("Tenha um bom dia! Dirija com segurança!")