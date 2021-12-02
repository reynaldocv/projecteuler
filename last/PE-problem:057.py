#Problem 057 : Square root convergents
import datetime

def program():
	lim = 1000
	num, den = 1, 1
	ans = 0
	for i in range(lim):
		num, den = den*2 + num, num + den
		if len(str(num)) > len(str(den)):
			ans += 1

	return ans
		
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 057 (", h2 - h1, ") : ", ans)


