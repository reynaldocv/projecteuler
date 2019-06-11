#Problem 005: Smallest multiple
import datetime

def program():	
	def MCD(a, b):
		if a % b == 0:
			return b
		else:
			return MCD(b, a % b)
	def mcm(a,b):
		return a*b//MCD(a,b)
	
	ans, nro = 2, 20
	for i in range(3, nro + 1):
		ans = mcm(ans, i)
	return ans
		

if __name__ == "__main__":
	h1 = datetime.datetime.now()	
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 005 (",h2 - h1,") : ", ans)
