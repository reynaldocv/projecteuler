#Problem 9: Special Pythagorean triplet
import datetime

def program():
	sum = 1000
	for S in range(sum - 1, 1, -1):
		R = ((sum - S)**2)/S	
		if S > R and R==int(R):
			c = (S+R)/2
			b = (S-R)/2
			a = sum - c - b	
			if a==int(a) and b==int(b) and c==int(c):				
				return int(c*b*a)

		
	
if __name__ == "__main__":
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 009 (",h2 - h1,") : ", ans)

