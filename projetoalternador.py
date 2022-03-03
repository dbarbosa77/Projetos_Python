


codigo = 'A1B2C3D4E5'






lista1 = []
lista2 = []



codigodividid = list(codigo)




for letra in codigodividid:

    if letra.isdigit():
            lista1.append(letra)

            
        
    else:
            lista2.append(letra)

            

        
print(f'essa é a lista 1 : {lista1}')
print(f'essa é a lista 2 : {lista2}')
