cnpj=input("Digite um CNPJ: ")       


remover="./-"                                         #For e variável "remover" utilizada somente para remover os caracteres indesejados do cnpj
for x in range(len(remover)):                          
    cnpj=cnpj.replace(remover[x],"")

novo_cnpj=cnpj[:12]                                    

total= 0
multiplicador = 5
multiplicador2 = 9

for numero in range(12):                                    
    if multiplicador > 1 and multiplicador <= 5:           # O if vai multiplicar os primeiros 4 numeros no CPF respectivamente por: 5,4,3,2
        total += int(novo_cnpj[numero]) * multiplicador 
        multiplicador = multiplicador - 1               
    else:                                                  # O else vai multiplicar o restante dos numeros do CPF respectivamente por: 9,8,7..
        total +=int(novo_cnpj[numero])*multiplicador2   
        multiplicador2 = multiplicador2 - 1             


d = 11 - (total % 11)                                      # Formula para descobrir o primeiro dígito.
if d > 9:
    d=0

multiplicador = 6                                          # A partir daqui o processo todo é refeito novamente para descobrir o segundo dígito
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
                    #Nessa etapa, vamos colocar o segundo dígito e após isso, formatar o cnpj e o novo_cnpj para a formatação de qualquer CNPJ
novo_cnpj = novo_cnpj + str(d2)
novo_cnpj = '{}.{}.{}/{}-{}'.format(novo_cnpj[:2], novo_cnpj[2:5], novo_cnpj[5:8], novo_cnpj[8:12],novo_cnpj[12:])
cnpj = '{}.{}.{}/{}-{}'.format(cnpj[:2],cnpj[2:5],cnpj[5:8],cnpj[8:12],cnpj[12:])
                    #Na ultima etapa, vamos somente confirmar se é válido ou não.
if novo_cnpj == cnpj:
    print(f"O CNPJ: {cnpj} é válido.")
elif not novo_cnpj == cnpj:
    print(f"o CNPJ: {cnpj} NÃO é válido.")










        
        
    
