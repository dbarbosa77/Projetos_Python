x = 0

n = int(input("A tabuada de qual numero você deseja ver?"))



for x in range(100): 
    if x < 100:
        taboada = x * n
        print(f'{x} x {n} = {taboada}')
        x+=1
    else:
        break
    




