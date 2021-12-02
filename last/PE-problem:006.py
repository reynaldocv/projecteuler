#Problem 006: Sum square difference
import datetime

def program():
	nro = 100
	return (nro*(nro+1)//2)**2 - (nro*(nro+1)*(2*nro+1))//6

if __name__ == "__main__":
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 006 (",h2 - h1,") : ", ans)

