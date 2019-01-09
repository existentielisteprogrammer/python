def main():
	number=int(input("n?"))
	val_numbers = [number]
	rest = []
	n = 0
	s = []
	while number >= 1:
		div = int(number/2)
		val_numbers.append(div)
		r = val_numbers[n] - (2*val_numbers[n+1])
		rest.append(r)
		number = div
		n += 1

		print("2*",val_numbers[n],"+",r,"q_n=",div,"r_n=",r)
	while n>0:
		n -= 1
		binaire = rest[n]
		s.append(binaire)
	print(val_numbers[0],"_10","=" ,s)
if __name__ == "__main__":
    main()
