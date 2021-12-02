#Problem 087 : Prime power triples
import datetime

def program():	
	lim = 50*10**6
	lim_ = int(lim**(.5)) + 1
	nros = [1 for i in range(lim_ + 1)]	
	primes = []
	
	for nro in range(2, lim_ + 1):
		if nros[nro] == 1:
			primes.append(nro)
			for mul in range(2*nro, lim_ + 1, nro):
				nros[mul] = 0

	nros = set([])
	for primeA in primes:
		for primeB in primes:
			sum_ = primeA**2 + primeB**3
			if sum_ >= lim:
				break
			else:
				for primeC in primes:
					sum__ = sum_ + primeC**4
					if sum__ >= lim:
						break
					else:
						nros.add(sum__)
	
	return len(nros)

	



			

		
 
	

if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 087 (", h2 - h1, ") : ", ans)

