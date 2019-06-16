#Problem 052 : Permuted multiples
import datetime

def program():		
	def digits(nro):
		digs = [l for l in str(nro)]
		digs.sort()
		return "".join(digs)

	dig = 1
	while True:
		for nro in range(10**dig, 10**(dig + 1)//6 + 1):
			digits_1 = digits(nro)
			permuted = True
			for mul in range(6, 1, -1):
				if digits(mul*nro) != digits_1:
					permuted = False
					break			
			if permuted: 
				return nro
		dig += 1		
		
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 052 (", h2 - h1, ") : ", ans)

