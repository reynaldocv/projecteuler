#Problem 068 : Magic 5-gon ring
import datetime

def program():	
	def permutation(numbers, temp, ans):
		if len(numbers) == 0:
			ans.append(temp)
		else:
			for i in range(len(numbers)):
				temp_ , numbers_ = temp.copy(), numbers.copy()				
				numbers_.pop(i)
				temp_.append(numbers[i])
				permutation(numbers_, temp_, ans)
		return ans
	
	f = 6 
	sum_ = 14
	ans = []
	for [a, b, c, d, e] in permutation([1, 2, 3, 4, 5], [], []):
		for [g, h, i, j] in permutation([7, 8, 9, 10], [], []):
			if f + a + b == g + b + c == h + c + d == e + d + i == a + e + j == sum_:
				aux = [f, a, b, g, b, c, h, c, d, i, d, e, j, e, a]
				aux = map(str, aux)
				ans.append("".join(aux))
	return max(ans)

			
		
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 068 (", h2 - h1, ") : ", ans)

