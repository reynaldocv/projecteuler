#Problem 4: Largest palindrome product
import datetime

def program():	
	nros = []
	for a in range(1,10):
		for b in range(0,10):
			for c in range(0,10):
				nros.append(100001*a+10010*b+1100*c)
				nros.append(10001*a+1010*b+100*c)	
	
	nros.sort(reverse=True)
	for nro in nros:
		x = max(100, int(nro**(.5)))
		y = nro//x
		while 100 <= x < 1000 and 100 <= y < 1000:
			if x*y == nro:
				return nro
			x += 1		
			y = nro//x

if __name__ == "__main__":
	h1 = datetime.datetime.now()	
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 004 (",h2 - h1,") : ", ans)
