#Problem 039 : Integer right triangles
import datetime

def program():	
	lim = 1000
	lim_ = lim//3 + 1
	perimeters = {}
	ans = (0, 0)
	for a in range(lim_):
		for b in range(a + 1, 2*lim_):
			c = (a**2 + b**2)**(.5)
			if c == int(c) and a + b + c <= lim:
				c = int(c)	
				perimeters[a + b + c] = perimeters.get(a + b + c, 0) + 1
				ans = max(ans, (perimeters[a + b + c], a + b + c))
			
	return ans[1]	
	
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 039 (", h2 - h1, ") : ", ans)

