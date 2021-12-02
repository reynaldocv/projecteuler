#Problem 3: Largest prime factor
import datetime

def program():	
	nro = 600851475143
	rpta = 3
	while nro > 2:
		if nro%rpta == 0:
			nro = nro/rpta	
		else:
			if rpta%10 == 3:
				rpta += 4
			else:
				rpta += 2
	return rpta	

if __name__ == "__main__":
	h1 = datetime.datetime.now()	
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 003 (",h2 - h1,") : ", ans)
