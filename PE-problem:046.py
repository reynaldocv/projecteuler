#Problem 046 : Goldbach's other conjecture
import datetime

def program():	
	def is_prime(nro, primes):
		lim = int(nro**(.5)) + 1
		for prime in primes:
			if nro % prime == 0:
				return False
			if prime > lim:
				break
		return True
	
	primes = [2, 3, 5, 7]
	nro = 9 
	while True: 
		if is_prime(nro, primes):
			primes.append(nro)
		else:			
			goldbach = False
			for prime in primes:
				x = (((nro - prime)//2)**(.5))
				if x == int(x):
					goldbach = True
					break
			if not goldbach:
				return nro
		nro += 2
	
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 041 (", h2 - h1, ") : ", ans)

