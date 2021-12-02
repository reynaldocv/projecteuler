#Problem 027 : Quadratic primes
import datetime

def program():	
	
	lim = 1000
	lim_ = lim**2 + lim*lim + lim

	primes = [1 for i in range(lim_)]	
	primes[0] = primes[1] = 0
	for nro in range(2, lim_):
		if primes[nro] == 1:	
			for mul in range(2*nro, lim_, nro):
				primes[mul] = 0
			
	ans = (39, 1, 41)	
	for b in range(3, lim, 2):
		if primes[b]:			
			for a in range(-b, lim, 2):
				if primes[ans[0]**2 + a*ans[0] + b]:	
					n = 1
					while primes[n**2 + a*n + b]:
						n += 1					
					ans = max(ans,(n, a, b))
				
	return ans[1]*ans[2]
			
					
					
		
	

	
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 027 (", h2 - h1, ") : ", ans)

