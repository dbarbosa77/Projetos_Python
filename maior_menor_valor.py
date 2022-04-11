a=int(input("Primeiro valor: "))
b=int(input("Segundo valor: "))
c=int(input("Terceiro valor: "))

if a<b and a<c:
    print(f"O menor valor digitado foi {a}.")
elif b<c and b<a:
    print(f"O menor valor digitado foi {b}.")
elif c<b and c<a:
    print(f"O menor valor digitado foi {c}.")
else:
    pass

if a>b and a>c: 
    print(f"O maior valor digitado foi {a}.")
elif b>c and b>a: 
    print(f"O maior valor digitado foi {b}.")
elif c>b and c>a:
    print(f"O maior valor digitado foi {c}.")
else:
    pass