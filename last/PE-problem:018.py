#Problem 018: Maximum path sum I
import datetime

def program():	
	def max_sum(data):
		n = len(data)
		for i in range(n-2 , -1, -1):
			for j in range(i+1):
				data[i][j] += max(data[i+1][j], data[i+1][j+1])	
		return data[0][0]

	file = open('PE-txt/PE-problem 018_in.txt')
	data = []
	for line in file:
		line = line.replace('\n','')		
		data.append([int(a) for a in line.split(" ")])
		
	return max_sum(data)
	rpta=0
	

if __name__ == "__main__":
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 018 (",h2 - h1,") : ", ans)

