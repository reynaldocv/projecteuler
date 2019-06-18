#Problem 082 : Path sum: three ways
import datetime

def program():	
	file = open("PE-txt/PE-problem 082_matrix.txt")
	data = []
	for line in file:
		line = line.replace("\n", "")
		data.append([int(a) for a in line.split(",")])
	
	lim = len(data)
	ans = []
	for i in range(lim):
		ans.append(data[i][0])
		
	ans2 = [0]*lim

	for i in data:
		print(i)
	print("---")
	for col in range(1, lim):
		for row in range(0, lim):
			ans[row] += data[row][col]
		print(ans)
		ans2[0] = min([ans[0], ans[1] + data[0][col]])
		for row in range(1, lim - 1):
			ans2[row] = min([ans2[row], ans[row - 1] +  data[row][col], ans[row + 1] +  data[row][col]])
		ans2[lim - 1] = min([ans2[lim - 1], ans[lim - 2] + data[lim - 1][col]])
		
		ans = ans2
		print(ans)
	
	return min(ans)
	
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 082 (", h2 - h1, ") : ", ans)

