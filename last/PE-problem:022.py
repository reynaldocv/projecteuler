#Problem 022 : Names scores
import datetime

def program():	
	def value_word(name):
		ans = 0
		for letter in name: 
			ans += ord(letter) - 64
		return ans
	
	file = open('PE-txt/PE-problem 022_names.txt')
	data = []
	for line in file:
		line = line.replace('\n','')	
		line = line.replace('"','')		
		data = line.split(",")	
	data.sort()
	
	ans = 0
	for i in range(len(data)):
		ans += (i+1)*value_word(data[i])
		
	return ans

if __name__ == "__main__":
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 022 (", h2 - h1, ") : ", ans)

