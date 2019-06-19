#Problem 011: Largest product in a grid
import datetime

def program():
	file = open("PE-txt/PE-problem 011_in.txt")
	data = []
	for line in file:
		line = line.replace("\n", "")
		data.append([int(a) for  a in line.split(" ")])

	lim = len(data)
	ans = 0
	for r in range(lim):
		for c in range(lim):
			if r >= 3:
				ans = max(ans, data[r][c]*data[r][c-1]*data[r][c-2]*data[r][c-3])
			if c >= 3:
				ans = max(ans, data[r][c]*data[r-1][c]*data[r-2][c]*data[r-3][c])
			if r >= 3 and c >= 3:
				ans = max(ans, data[r][c]*data[r-1][c-1]*data[r-2][c-2]*data[r-3][c-3])
			if r >= 3 and c < lim - 3:
				ans = max(ans, data[r][c]*data[r-1][c+1]*data[r-2][c+2]*data[r-3][c+3])

	return ans

if __name__ == "__main__":
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 011 (",h2 - h1,") : ", ans)

