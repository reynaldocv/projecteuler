#Problem 067 : Maximum path sum II
import datetime

def program():		
	file = open("PE-txt/PE-problem 067_triangle.txt")
	data = []
	for line in file: 
		line = line.replace("\n","")
		data.append([int(a) for a in line.split(" ")])

	for row in range(len(data) - 2, -1, -1):
		for i in range(len(data[row])):
			data[row][i] += max(data[row + 1][i], data[row + 1][i + 1])

	return data[0][0]	
		
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 067 (", h2 - h1, ") : ", ans)

