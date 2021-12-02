#Problem 021 : Amicable numbers 
import datetime

def program():	
	lim = 10000
	sum_div = [1 for i in range(lim)]
	
	for div in range(2,lim):
		for mul in range(2*div, lim, div):
			sum_div[mul] += div
	
	ans = 0
	for nro in range(2,lim):
		aux = sum_div[nro] 
		if aux <= lim and sum_div[aux] == nro and aux != nro:
			ans += nro
	return ans

if __name__ == "__main__":
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 021 (", h2 - h1, ") : ", ans)

