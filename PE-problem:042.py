#Problem 042 : Coded triangle numbers
import datetime

def program():	
	def sum_letters(word):
		ans = 0
		for w in word:
			ans += ord(w) - 64
		return ans

	def is_triangle(nro):
		aux = int((nro*2)**(.5))
		return aux*(aux + 1)//2 == nro

	file = open("PE-txt/PE-problem 042_words.txt")
	words = []
	for line in file:
		line = line.replace('"',"")
		words = line.split(",")
	
	ans = 0
	for word in words:
		if is_triangle(sum_letters(word)):
			ans += 1

	return ans
	
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 042 (", h2 - h1, ") : ", ans)

