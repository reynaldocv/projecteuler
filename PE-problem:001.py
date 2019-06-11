#Problem 001: Multiples of 3 and 5
import datetime

def program():
	def suma(m, n):
		return m*((n - 1)//m)*((n - 1)//m + 1)//2

	return suma(3, 1000)+suma(5, 1000)-suma(15, 1000)

if __name__ == "__main__":
	h1 = datetime.datetime.now()	
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 001 (",h2 - h1,") : ",ans)
