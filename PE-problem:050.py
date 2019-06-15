#Problem 050 : Consecutive prime sum
import datetime

def program():		
	lim = 1000000
	nros = [0 for i in range(lim)]
	primes = []
	for nro in range(2, lim):
		if nros[nro] == 0: 
			primes.append(nro)
			for mul in range(2*nro, lim, nro):
				nros[mul] = 1
	
	ans = (2, 5)
	for i in range(len(primes)):
		for j in range(i+2, len(primes)):
			sum_ = sum(primes[i: j])
			if sum_ > lim:
				break
			if sum_ < lim and nros[sum_] == 0:
				ans = max(ans, (j-i, sum_))

	return ans[1]				
		
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 050 (", h2 - h1, ") : ", ans)

