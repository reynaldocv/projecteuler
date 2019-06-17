#Problem 069 : Totient maximum
import datetime

def program():	
	lim = 10**6
	phi = [nro for nro in range(lim + 1)]
	ans = (2, 2)
	for nro in range(2, lim + 1):
		if phi[nro] == nro:
			for mul in range(nro, lim + 1, nro):
				phi[mul] *= (nro - 1) 
				phi[mul] //= nro
		ans = max(ans, (nro/phi[nro], nro))
	
	return ans[1]
		 

			
		
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 069 (", h2 - h1, ") : ", ans)

