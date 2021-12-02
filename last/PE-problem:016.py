#Problem 016: Power digit sum
import datetime

def program():
	nro = 2**1000
	ans = 0
	while nro > 0:
		ans += nro%10	
		nro //= 10
	return ans

if __name__ == "__main__":
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 016 (",h2 - h1,") : ", ans)

