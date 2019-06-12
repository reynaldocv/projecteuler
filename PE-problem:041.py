#Problem 041 : Pandigital prime
import datetime

def program():	
	def is_prime(nro):
		lim = int(nro**(.5)) + 1
		for i in range(3, lim, 2):
			if nro % i == 0:	
				return False
		return True
			

	def gen_odd_pandigital(word, letters, rpta):
		if letters != "":
			for l in letters:
				gen_odd_pandigital(word+l, letters.replace(l,""),rpta)
		else:			
			rpta.append(int(word))
	
	pandigitals = []
	gen_odd_pandigital("", "7654321", pandigitals)
	gen_odd_pandigital("", "4321", pandigitals)
	
	for pandigital in pandigitals:
		if pandigital % 2 == 1:
			if is_prime(pandigital):
				return pandigital

	
		
	
	

	
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 041 (", h2 - h1, ") : ", ans)

