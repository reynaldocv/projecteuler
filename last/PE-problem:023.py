#Problem 023 : Non-abundant sums
import datetime

def program():	
	lim = 28123
	sum_div = [1 for i in range(lim)]
	abundants = []	

	for div in range(2, lim):
		if div < sum_div[div] and sum_div[div] < lim:
			abundants.append(div)
		for mul in range(2*div, lim, div):
			sum_div[mul] += div
	
	numbers = set([])	
	for nroA in abundants:
		for nroB in abundants:
			aux = nroA + nroB 
			if nroA + nroB > lim:
				break
			numbers.add(aux)

	return lim*(lim+1)//2 - sum(numbers)

if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 023 (", h2 - h1, ") : ", ans)

