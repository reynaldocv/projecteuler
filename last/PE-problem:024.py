#Problem 024 : Lexicographic permutations
import datetime

def program():	
	def factorial(n):
		return 1 if n < 2 else n*factorial(n-1)

	n, n_th = 10, 999999
	values = [str(i) for i in range(n)]
	fact = factorial(n-1)
	ans = ""	

	while n_th > 0:	
		n -= 1		
		pos = n_th//fact
		ans += values[pos]
		values.pop(pos)
		n_th = n_th % fact
		fact //= n

	return ans + "".join(values)
	

if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 024 (", h2 - h1, ") : ", ans)

