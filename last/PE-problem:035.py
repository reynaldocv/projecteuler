#Problem 035 : Circular primes
import datetime

def program():	
	def digits(nro):
		digs = [l for l in str(nro)]
		digs.sort()
		return "".join(digs)
	
	lim = 10**6
	
	nros = [1 for i in range(lim)]	
	group = {}
	for nro in range(2, lim):
		if nros[nro] == 1:	
			digs = digits(nro)
			group[digs] = group.get(digs,[])
			group[digs].append(nro)									
			for mul in range(2*nro, lim, nro):
				nros[mul] = 0
	
	ans = set([])
	for nro in group:
		for prime in group[nro]:
			if prime not in ans:
				is_cycle = True
				for rot in range(len(str(prime))):
					aux = int(str(prime)[rot - 1:] + str(prime)[:rot - 1])
					if nros[aux] != 1:
						is_cycle = False
						break
				if is_cycle:
					for rot in range(len(str(prime))):
						aux = int(str(prime)[rot - 1:] + str(prime)[:rot - 1])
						ans.add(aux)

	return len(ans)
	
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 035 (", h2 - h1, ") : ", ans)

					

