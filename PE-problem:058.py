#Problem 058 : Spiral primes
import datetime

def program():
	def is_prime(nro):
		lim = int(nro**(.5)) + 1
		for i in range(3, lim, 2):
			if nro % i == 0:
				return False
		return True

	nro, cycle, primes, nros = 1, 1, 0, 1
	while True:
		for i in range(4):
			nro += 2*cycle
			if is_prime(nro):
				primes += 1
		nros += 4
		if primes/nros < 1/10:
			return 2*cycle + 1
		cycle += 1



		
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 058 (", h2 - h1, ") : ", ans)


