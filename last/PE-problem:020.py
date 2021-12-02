#Problem 020: Factorial digit sum
import datetime

def program():	
	nro = 100
	mul = 1	
	ans = 0
	for i in range(2, nro+1):
		mul *= i
	while mul > 0:
		ans += mul % 10
		mul //= 10
	return ans

if __name__ == "__main__":
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 020 (", h2 - h1, ") : ", ans)

