#Problem 049 : Prime permutations
import datetime

def program():	
	def digits(nro):
		nro = [l for l in str(nro)]
		nro.sort()
		return "".join(nro)
	
	lim = 10000
	primes = [0 for i in range(lim)]
	group = {}
	for nro in range(2, lim):
		if primes[nro] == 0: 
			if nro > 1000:
				digits_ = digits(nro)
				group[digits_] = group.get(digits_, [])
				group[digits_].append(nro)
			for mul in range(2*nro, lim, nro):
				primes[mul] = 1
	
	nros = []
	for digits_ in group.keys():
		for i in range(len(group[digits_])):
			for j in range(i + 1, len(group[digits_])):
				for k in range(j + 1, len(group[digits_])):
					aux1 = group[digits_][k] - group[digits_][j]
					aux2 = group[digits_][j] - group[digits_][i] 
					if  aux1 == aux2 :
						aux3 = str(group[digits_][i])
						aux3 += str(group[digits_][j])
						aux3 += str(group[digits_][k])
						nros.append(aux3)

	for nro in nros:
		if nro != "148748178147":
			return nro
		
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 049 (", h2 - h1, ") : ", ans)

