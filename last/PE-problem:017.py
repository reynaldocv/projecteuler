#Problem 017 : Number letter counts
import datetime 

def program():		
	u = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
	d = [0,0,6,6,5,5,5,7,6,6]
	c = [u[i] + 7 for i in range(10)]
	c[0] = 0	
	ans = 0
	for nro in range(1,1000):
		ans += c[nro//100]		
		if nro % 100 != 0:
			if nro//100 != 0:
				ans += 3
			if nro % 100 < 20:
				ans += u[nro % 100]
			else:
				ans += d[(nro % 100)//10] + u[nro % 10]
	return ans + 11

if __name__ == "__main__":
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 017 (",h2 - h1,") : ", ans)

