#Problem 007: 10001st prime
import datetime
import math

def program():
	def nro_max(n):
		lim = n
		while lim/math.log(lim) < n:
			lim += 1
		return lim
	
	i_th = 10001
	lim, i = nro_max(i_th), 0
	
	nros = [1 for a in range(lim)]
	for j in range(2,lim):		
		if nros[j] == 1:
			i+=1			
			for k in range(2*j, lim, j):
				nros[k] = 0
			if i == i_th:
				return j

if __name__ == "__main__":
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 007 (",h2 - h1,") : ", ans)

