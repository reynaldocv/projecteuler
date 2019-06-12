#Problem 014: Longest Collatz sequence
import datetime

def program():
	lim = 1000000
	collatz = {1:1}
	def sequence(nro):
		aux = collatz.get(nro, 0)
		if aux == 0:
			if nro % 2 == 0:	
				collatz[nro] = 1 + sequence(nro//2)
			else: 
				collatz[nro] = 1 + sequence(nro*3 + 1)
		return collatz[nro]
		
	ans = [1,1]
	for i in range(2, lim):
		ans = max(ans, [sequence(i), i])

	return ans[1]
			
	
if __name__ == "__main__":
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 014 (",h2 - h1,") : ", ans)

