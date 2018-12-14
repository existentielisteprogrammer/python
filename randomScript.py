import random
def alea() :
	a = random.random()*100
	a=round(a)
	return a
	
b=1
c=0
while b<1000 :
	b=b+1
	if alea()==100 :
		c=c+1
e='il y a eu '
f=' fois le nombre 100.'


print(e+str(c)+f)
