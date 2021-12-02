#Problem 072 : Counting fractions
import datetime

def program():	
	lim = 10**6
	phi = [nro for nro in range(lim + 1)]
	phi[0] = phi[1] = 0
	for nro in range(2, lim + 1):
		if phi[nro] == nro:
			for mul in range(nro, lim + 1, nro):
				phi[mul] *= (nro - 1)
				phi[mul] //= nro

	return sum(phi)
		
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 071 (", h2 - h1, ") : ", ans)

