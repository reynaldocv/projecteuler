#Problem 026 : Reciprocal cycles
import datetime

def program():	
	lim = 1000
	primes = [i%2 for i in range(lim)]
	for i in range(5, lim, 5):
		primes[i] = 0

	ans = [1,3]
	for nro in range(3,lim):
		if primes[nro] == 1:									
			for mul in range(2*nro, lim, nro):
				primes[mul] = 0

			nines, i = 9, 1
			while nines % nro != 0:
				i += 1
				nines = 10*nines + 9
			ans = max(ans, [i, nro])

	return ans[1]
	

	
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 026 (", h2 - h1, ") : ", ans)

