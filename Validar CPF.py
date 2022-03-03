cpf= input('Qual seu cpf? apenas os números ')
novo_cpf = cpf [:9]
reverso = 10
total= 0

for numero in range(19):
    if numero > 8:
        numero -= 9
    
    total += int(novo_cpf[numero]) * reverso
    reverso -=1 

    
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total=0
        novo_cpf += str(d)

print(novo_cpf)

if cpf == novo_cpf:
    print('O CPF É VÁLIDO')
    
else:
    print('O CPF É INVÁLIDO')


      