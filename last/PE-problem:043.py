#Problem 043 : Sub-string divisibility
import datetime

def program():
	def repeated_digits(str_nro):
		repeat = {}
		for digit in str_nro:
			if digit in repeat:
				return True
			else:
				repeat[digit] = 1
		return False
				
	divisors = [13, 11, 7, 5, 3, 2,1]		
	nros = []

	for str_nro in [str(nro) for nro in range(17, 1000, 17)]:
		if repeated_digits(str_nro) == False:
			if len(str_nro) == 2:
				nros.append("0" + str_nro)
			else: 
				nros.append(str_nro)			

	tens = 3
	for div in divisors:
		ans = []
		for nro in nros: 
			for n in range(10):
				if str(n) not in nro:
					nro_ = str(n) + nro
					if int(nro_)//(10**(tens - 2)) % div == 0:
						if not repeated_digits(nro_):
							ans.append(nro_)
		nros = ans		
		tens += 1	
	nros = map(int, nros)

	return sum(nros)
	
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 043 (", h2 - h1, ") : ", ans)

