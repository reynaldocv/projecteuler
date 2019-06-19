#Problem 062 : Cubic permutations
import datetime

def program():
	def digits(nro):
		digs = [str(l) for l in str(nro)] 
		digs.sort()
		return "".join(digs)
	
	permutations = {}	
	nro = 2
	while True:
		digs = digits(nro**3)
		permutations[digs] = permutations.get(digs, [])
		permutations[digs].append(nro**3)
		if len(permutations[digs]) == 5:			
			return min(permutations[digs])
		nro += 1
			
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 062 (", h2 - h1, ") : ", ans)


