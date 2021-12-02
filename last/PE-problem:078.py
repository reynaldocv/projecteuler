#Problem 078 : Coin partitions 
import datetime
import math

def program():	
	def Pentagonal(nro):
		return nro*(3*nro - 1)//2

	lim = 10**6
	ways = {0: 1, 1: 1, 2: 2}
	nro = 2
	signs = [+1, +1, -1, -1]	
	while ways[nro] % lim != 0:
		nro += 1
		i, sum_, sign = -1, ways[nro - 1], 1 	
		while nro >= Pentagonal(i):			
			sum_ += signs[sign] * ways[nro - Pentagonal(i)]
			if i > 0:
				i *= -1
			else:
				i = -i + 1
			sign = (sign + 1) % 4
		ways[nro] = sum_

	return nro	
		
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 078 (", h2 - h1, ") : ", ans)

