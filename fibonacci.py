a=0
b=1
n = int(input("Vous voulais voir combien d'éléments de la suite fibonacci?"))
for i in range(n):
	print(a)
	temp = a
	a = b
	b = temp + b
