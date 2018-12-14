n = 0
def u(n):
	u = [3.5/128]
	for n in range(20):
		s = 3.5/128 * 2**n 
		u.append(s)
	print(u)
u(n)