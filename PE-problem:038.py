#Problem 038 : Pandigital multiples
import datetime

def program():	
	def repeated_digits(str_nro):
		digits = {}
		for l in str_nro:
			if l in digits or l == "0":
				return True
			else:
				digits[l] = 1
		return False

	for nro in range(9876, 1234, -1):
		nro2 = str(nro) + str(2*nro)
		if not repeated_digits(nro2):
			return nro2		
	
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 038 (", h2 - h1, ") : ", ans)

