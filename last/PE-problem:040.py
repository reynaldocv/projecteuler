#Problem 040 : Champernowne's constant
import datetime

def program():	
	def champernowne(i_th):
		dig = 1		
		while i_th > dig*9*10**(dig - 1):			
			i_th -= dig*9*10**(dig - 1)
			dig += 1
		nro = i_th//dig	
		pos = i_th%dig
		if pos == 0:
			nro -= 1
			pos = dig 	
		return int(str(10**(dig - 1) + nro)[pos - 1])
	
	ans = 1
	for i in range(1,7):
		ans *= champernowne(10**i)
	
	return ans

if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 040 (", h2 - h1, ") : ", ans)

