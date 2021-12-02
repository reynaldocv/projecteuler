#Problem 015: Lattice paths
import datetime

def program():
	m = 20
	n = 2*m
	ans = 1
	for i in range(m + 1, n + 1):
		ans *= i
	for i in range(2,m + 1):
		ans //= i

	return ans
	
if __name__ == "__main__":
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 015 (",h2 - h1,") : ", ans)

