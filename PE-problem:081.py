#Problem 081 : Path sum: two ways
import datetime

def program():	
	file = open("PE-txt/PE-problem 081_matrix.txt")
	data = []
	for line in file:
		line = line.replace("\n", "")
		data.append([int(a) for a in line.split(",")])
	
	lim = len(data)
	for i in range(1, lim):	
		data[0][i] += data[0][i - 1]
		data[i][0] += data[i - 1][0]
	for row in range(1, lim):
		for col in range(1, lim):
			data[row][col] += min(data[row - 1][col], data[row][col - 1])
	
	return data[lim - 1][lim - 1]
	
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 081 (", h2 - h1, ") : ", ans)

