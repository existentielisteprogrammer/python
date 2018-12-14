for i in range(0,1000):
	for entiersentre in range(2,i):
		if(i%entiersentre)==0:
			break
		elif(i%entiersentre!=0) and (entiersentre)==i-1:
			print(i)