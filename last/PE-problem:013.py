#Problem 013: 
import datetime

def program():
	file = open('PE-txt/PE-problem 013_in.txt')
	ans = 0
	for line in file:
		line = line.replace('\n','')		
		ans += int(line)

	return str(ans)[:10]
	
if __name__ == "__main__":
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 013 (",h2 - h1,") : ", ans)

