#Problem 077 : Prime summations
import datetime
import math

def program():	
	lim = 5000
	nros = [1 for nro in range(lim)]
	primes = []
	for nro in range(2, lim):
		if nros[nro] == 1:
			primes.append(nro)
			for mul in range(2*nro, lim, nro):
				nros[mul] = 0

	ways = [0 for a in range(lim)]
	ways[0] = 1
	for prime in primes:
		for nro in range(prime, lim):
			ways[nro] += ways[nro - prime]

	for nro in range(lim):
		if ways[nro] >= lim:
			return nro
		
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 077 (", h2 - h1, ") : ", ans)

