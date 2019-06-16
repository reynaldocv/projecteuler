#Problem 052 : Combinatoric selections
import datetime

def program():		
	lim = 100
	ans = 0
	for n in range(23, lim + 1):
		nro, num, den = n, n - 1, 2		
		for r in range(2, n//2 + 1):
			nro *= num
			nro //= den
			num, den = num - 1, den + 1
			if nro > 10**6:
				ans += n + 1 - 2*r
				break
	return ans		
		
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 053 (", h2 - h1, ") : ", ans)

