def main():
	messageAlice 	= "Bonjour Bob Comment ca va? Ca va fait grave longtemps qu'on ne s'est pas vu. T'es chaud on se fait McDO :P Tu te souviens de la soirée, bahhh ... enfaite je suis tombé enceinte et t'es le père du gosse, il a 3 mois, il s'appelle Bernard, il a le meme nez que toi, miskine, et heureusement qu'il me ressemble un peu plus que toi"
	key 			= [1,0,0,0,0,0, 0,0,0,0]
	messageCode		= ChiffrerDechiffreXOR(messageAlice,key)
	print(messageCode)

def convertirEnBinaire(choix) :
	binaire = [0,0,0,0,0,0,0,0]
	c = 0
	q = int(choix)
	dividende = q

	while q != 0 :
		if dividende % 2 == 1 :
			binaire [c] = 1
			c+=1
			q = q / 2 - 0.5
		else :
			binaire [c] = 0
			c+=1
			q /= 2 
		dividende = q
	binaire.reverse()
	return binaire	

#taille de key au moins 8 bits
#"clair" un string
def ChiffrerDechiffreXOR(clair,key) :
	messagefin = ""
	c=0
	for lettre in clair:
		codeascii= ord(lettre)
		convbin= convertirEnBinaire(codeascii)
		code = []
		for b in convbin:
			result = b^key[c]
			c+=1
			if c == len(key):
				c = 0 
			code.append(result) 
		
		codedeci=convertirEnDecimale(code)
		messagefin += chr(codedeci)
	return messagefin 
	
def convertirEnDecimale(m):
	n1 = len(m) - 1
	n =  0
	calcul = 0
	while n1 >= 0 :
		calcul += 2**n * m[n1]
		n += 1
		n1 -= 1
	return calcul
if __name__ == "__main__":
	main()
	
