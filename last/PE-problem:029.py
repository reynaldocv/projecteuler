#Problem 029 : Distinct powers
import datetime

def program():	
	ans = set([])
	for a in range(2, 101):
		for b in range(2, 101):
			ans.add(a**b)

	return len(ans)
	
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 029 (", h2 - h1, ") : ", ans)

