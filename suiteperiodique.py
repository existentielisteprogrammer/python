
def main():
	n = 0
	keys = [5] #keys[0] = 5
	calcul = 0 #calcul[0] = 0

	for _ in range(100):
		calcul = (2 * keys[n] + 7) % 26 
		n += 1
		if keys[0]==calcul: #if calcul = 5
			print("keys:",keys)
			print("sa période =",len(keys))
			break
		keys +=  [calcul] # c'est pareille avec keys.append(calcul)

main()
	