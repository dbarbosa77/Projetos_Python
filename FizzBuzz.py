n1=int(input("Digite um numero: "))



def numero(n1):
    if n1 % 5 == 0 and n1 % 3 ==0:
        return("FizzBuzz")
    elif n1 % 5 ==0:
        return('Buzz')
    elif n1 % 3 == 0:
        return("Fizz")
        
    else:
        return(n1)

edivisivelpor = numero(n1)

print(edivisivelpor)
