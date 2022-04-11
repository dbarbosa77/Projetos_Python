import datetime 
ano= int(input("Qual ano você deseja consultar? "))
current_time = datetime.datetime.now()


if ano == 0:
    ano = current_time.year
    
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano de {ano} é bissexto.")
else:
    print(f"O ano de {ano} NÃO é bissexto.")
    

    

