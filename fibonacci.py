a=0
b=1
n = int(input("Vous voulais voir combien d'éléments de la suite fibonacci?"))+1
for _ in range(n):
	print(a)
	temp = a
	a = b
	b = temp + b
"""Now code will give exect length of n.For example for n=12 output will be 0
1
1
2
3
5
8
13
21
34
55
89
144.For doing this n = int(input("Vous voulais voir combien d'éléments de la suite fibonacci?")) updated to n = int(input("Vous voulais voir combien d'éléments de la suite fibonacci?"))+1
"""