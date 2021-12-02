#Problem 048 : Self powers
import datetime

def program():
	lim = 1000
	ans = 0
	for i in range(1,lim + 1):
		ans = (ans + i**i) % 10**10
	return ans 
	
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 048 (", h2 - h1, ") : ", ans)

