#Problem 034 : Digit factorials
import datetime

def program():	
	def factorial(nro):
		return 1 if (nro < 2) else nro*factorial(nro-1)
	
	def sum_dig_fact(nro, facts):
		ans = 0
		while nro > 0:
			ans += facts[nro%10]
			nro //= 10
		return ans

	facts = [factorial(nro) for nro in range(10)]
	sums = [factorial(nro) for nro in range(10)]
	
	for time in range(2, 10):		
		aux = set([])
		for sum in sums:
			for fact in facts:
				aux.add(sum + fact)
		sums = aux

	ans = 0
	for sum in sums:
		if sum == sum_dig_fact(sum, facts):
			ans += sum
	
	return ans
	
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 034 (", h2 - h1, ") : ", ans)

