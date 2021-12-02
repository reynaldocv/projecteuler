#Problem 047 : Distinct primes factors
import datetime

def program():	
	lim = 10**6
	factors = [0 for i in range(lim)]
	for nro in range(2, lim):
		if factors[nro] == 0:
			for mul in range(2*nro, lim, nro):
				factors[mul] += 1

	count = 0 
	for nro in range(2, lim):
		if factors[nro]>= 4:
			count += 1
			if count == 4:
				return nro - 3	
		else:
			count = 0

if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 047 (", h2 - h1, ") : ", ans)

