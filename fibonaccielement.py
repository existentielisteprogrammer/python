a=1
b=1
n = int(input("Vous voulais voir quel élément de la suite de Fibonacci?"))
for i in range(n):
    c = a + b
    a = b
    b = c
print(a)