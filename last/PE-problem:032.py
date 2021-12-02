#Problem 032 : Pandigital products
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

	ans = set([])
	for nro in range(2, 10):
		for nro2 in range(1234, 10000//nro):
			if not repeated_digits(str(nro) + str(nro2) + str(nro*nro2)):
				ans.add(nro*nro2)

	for nro in range(11, 100):
		for nro2 in range(123, 10000//nro):
			if not repeated_digits(str(nro) + str(nro2) + str(nro*nro2)):
				ans.add(nro*nro2)
	
	return sum(ans)

if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 032 (", h2 - h1, ") : ", ans)

