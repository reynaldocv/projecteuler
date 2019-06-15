#Problem 044 : Pentagon numbers
import datetime

def program():	
	def is_Pentagon(nro):
		x = (1 + (1 + 24*nro)**(.5))/6
		return x == int(x)
	
	n = 2
	pentagons = [1]
	while True:
		Pn = n*(3*n - 1)//2
		for pentagon in pentagons:
			if is_Pentagon(pentagon + Pn):
				if is_Pentagon(Pn - pentagon):
					return Pn - pentagon
		pentagons.append(Pn)
		n += 1
	
		
		
	
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 044 (", h2 - h1, ") : ", ans)

