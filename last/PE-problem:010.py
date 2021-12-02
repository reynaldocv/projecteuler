#Problem 010: Summation of primes
import datetime

def program():
	lim = 2000000
	nros = [1 for i in range(lim)]
	ans = 0
	for i in range(2, lim):
		if nros[i] == 1:
			ans += i
			for j in range(2*i, lim, i):
				nros[j] = 0
	return ans
	
if __name__ == "__main__":
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 010 (",h2 - h1,") : ", ans)

