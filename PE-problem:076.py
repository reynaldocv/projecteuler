#Problem 076 : Counting summations
import datetime

def program():	
	lim = 100
	ways = [1 for i in range(lim + 1)]
	for dig in range(2, lim):
		for nro in range(dig, lim + 1):
			ways[nro] += ways[nro - dig]

	return ways[lim]
		
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 076 (", h2 - h1, ") : ", ans)

