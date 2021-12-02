#Problem 028 : Number spiral diagonals
import datetime

def program():	
	cycles = 1001
	cycle_lim = cycles//2 + 1		
	value = ans = 1
	for cycle in range(1, cycle_lim):
		razon = 2 * cycle
		for i in range(4):
			value += razon
			ans += value
	
	return ans
	
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 028 (", h2 - h1, ") : ", ans)

