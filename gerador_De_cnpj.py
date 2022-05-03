from random import randint
cnpj=str(randint(10000000, 99999999))   

novo_cnpj=cnpj[:8] + "0001"
                 
total= 0
multiplicador = 5
multiplicador2 = 9

for numero in range(12):                                    
    if multiplicador > 1 and multiplicador <= 5:           
        total += int(novo_cnpj[numero]) * multiplicador 
        multiplicador = multiplicador - 1               
    else:                                                  
        total += int(novo_cnpj[numero]) * multiplicador2 
        multiplicador2 = multiplicador2 - 1             

d = 11 - (total % 11)                                      
if d > 9:
    d=0

multiplicador = 6                                          
total2 = 0
multiplicador2 = 9
novo_cnpj = novo_cnpj + str(d)

for numero in range(13):
    if multiplicador > 1 and multiplicador <= 6:
        total2 += int(novo_cnpj[numero]) * multiplicador
        multiplicador = multiplicador - 1
    else:
        total2 +=int(novo_cnpj[numero])*multiplicador2
        multiplicador2 = multiplicador2 - 1
d2= 11 - (total2 % 11)
if d2 > 9:
    d2=0                  
    
novo_cnpj = novo_cnpj + str(d2)
novo_cnpj = '{}.{}.{}/{}-{}'.format(novo_cnpj[:2], novo_cnpj[2:5], novo_cnpj[5:8], novo_cnpj[8:12],novo_cnpj[12:])
cnpj = '{}.{}.{}/{}-{}'.format(cnpj[:2],cnpj[2:5],cnpj[5:8],cnpj[8:12],cnpj[12:])

print(novo_cnpj)

