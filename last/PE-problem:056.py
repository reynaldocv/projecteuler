#Problem 056 : Self powers
import datetime

def program():
	def sum_digits(nro):
		ans = 0
		while nro > 0:
			ans += nro % 10
			nro //= 10
		return ans

	lim = 100
	ans = 1
	for a in range(1, lim + 1):	
		for b in range(1, lim + 1):
			ans = max(ans, sum_digits(a**b))

	return ans
		
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 056 (", h2 - h1, ") : ", ans)


