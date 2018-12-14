# ce code a été fait par Ow ow.charlon@gmail.com 
# ce code est sous licence wtfpl

import random

def Hasard(a) :
	liste1 = ""
	while len(liste1) < a :
		liste1 = liste1 + chr(random.randint(97, 122))
	
	return str(liste1)
	
count = 1
while count < 100000 :
	print(Hasard(count))
	count += 1