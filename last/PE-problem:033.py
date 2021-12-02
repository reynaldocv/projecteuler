#Problem 033 : Digit cancelling fractions
import datetime

def program():	
	def MCD(a, b):
		return b if (a % b == 0) else MCD(b, a % b)

	num = den = 1
	for a in range(1, 10):
		for c in range(a + 1, 10):
			for b in range(1, 10):
				if a/b == ((10*a + c)/(10*c + b)):
					num *= a
					den *= b
		
	return den//MCD(num, den)

if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 033 (", h2 - h1, ") : ", ans)

