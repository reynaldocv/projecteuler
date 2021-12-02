#Problem 099 : Largest exponential
import datetime
import math
def program():	
	file = open("PE-txt/PE-problem 099base_exp.txt")
	data = []	
	for line in file:
		line = line.replace("\n","")
		data.append([int(a) for a in line.split(",")])
		
	ans = (-1, -1)		
	for i in range(len(data)):
		base = data[i][0]
		exp = data[i][1]
		ans = max(ans, (exp*math.log(base), i))

	return ans[1] + 1

if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 099 (", h2 - h1, ") : ", ans)

