#Problem 012: Highly divisible triangular number
import datetime

def program():
	max_div = 500
	lim = 3*5*7*11*13*17
	divisors = [1 for x in range(lim)]	
	for nro in range(2, lim):
		for mul in range(nro, lim, nro):
			divisors[mul] += 1
		if nro % 2 == 0:
			n_div = divisors[nro//2] * divisors[nro-1]
		else: 
			n_div = divisors[nro] * divisors[(nro-1)//2]
		if n_div > max_div:				
			return (nro-1)*nro//2
	
if __name__ == "__main__":
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 012 (",h2 - h1,") : ", ans)

