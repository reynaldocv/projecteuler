#Problem 030 : Digit fifth powers
import datetime

def program():	
	def sum_dig_pow(nro):
		ans = 0
		while nro > 0:
			ans += (nro % 10)**5
			nro //= 10
		return ans
		
	sums = [i**5 for i in range(2,10)]
	power = [i**5 for i in range(10)]

	for time in range(6):
		aux = set([])	
		for sum in sums:			
			for i in range(10): 
				sum_ = sum + power[i]
				if sum_ < 10**6:
					aux.add(sum_)
				else:
					break
		sums = aux

	ans = 0
	for sum in sums:
		if sum == sum_dig_pow(sum):
			ans += sum
			
	return ans
	
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 030 (", h2 - h1, ") : ", ans)

