#Problem 045 : Triangular, pentagonal, and hexagonal
import datetime

def program():	
	def is_Pentagon(nro):
		x = (1 + (1 + 24*nro)**(.5))/6
		return x == int(x)

	def is_Triangle(nro):
		x = (-1 + (1 + 8*nro)**(.5))/2
		return x == int(x)

	
	n = 144
	while True:
		Hn = n*(2*n - 1)	
		if is_Pentagon(Hn) and is_Triangle(Hn):
			return Hn
		n += 1
	
		
		
	
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 041 (", h2 - h1, ") : ", ans)

