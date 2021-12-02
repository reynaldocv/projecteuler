#Problem 002: Even Fibonacci numbers
import datetime 

def program():
	ans = g1 = 2
	g2 = 8
	while g2 < 4000000:		
		ans += g2	
		aux = g2
		g2 = g1 + 4*g2
		g1 = aux
	return ans

if __name__ == "__main__":
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 002 (",h2 - h1,") : ",ans)

