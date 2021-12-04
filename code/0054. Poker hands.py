from collections import defaultdict

class solution:
	def solution0054(self):
		def helper(arr): 
			numbers = defaultdict(lambda: 0)
			types = defaultdict(lambda: 0)
			for card in arr: 
				numbers[values[card[0]]] += 1
				types[card[1]] += 1
			
			if len(numbers) == 5:
				if min(numbers.keys()) + 4 == max(numbers.keys()):
					if len(types) == 1: 
						ans = (9,) + tuple(sorted(numbers.keys(), reverse = True))
					else: 
						ans = (5,) + tuple(sorted(numbers.keys(), reverse = True))
				
				elif len(types) == 1: 
					ans = (6,) + tuple(sorted(numbers.keys(), reverse = True))		
				else: 
					ans = (1,) + tuple(sorted(numbers.keys(), reverse = True))
				
			elif len(numbers) == 4: 
				ans =  (2,) + tuple([key for key in numbers if numbers[key]== 2]*2) 
				ans += tuple(sorted([key for key in numbers if numbers[key]== 1], reverse = True))
				
			elif len(numbers) == 3:
				if max(numbers.values()) == 3: 
					ans = (4,) + tuple([key for key in numbers if numbers[key]== 3]*3) 
					ans += tuple(sorted([key for key in numbers if numbers[key]== 1], reverse = True))
					
				else:
					ans = (3,) + tuple(sorted([key for key in numbers if numbers[key]== 2]*2, reverse = True)) 
					ans += tuple([key for key in numbers if numbers[key]== 1])
				
			elif len(numbers) == 2: 
				if max(numbers.values()) == 4: 
					ans = (8,) + tuple(sorted([key for key in numbers if numbers[key] == 4]*4)) 
					ans += tuple(sorted([key for key in numbers if numbers[key] == 1]))
				else: 
					ans = (7,) + tuple(sorted([key for key in numbers if numbers[key] == 3]*3)) 
					ans += tuple(sorted([key for key in numbers if numbers[key] == 2]*2))
				
			return ans
				
		ans = 0

		values = {"A": 14, "K":13, "Q": 12, "J": 11, "T": 10}
		for i in range(2, 10):
			values[str(i)] = i

		file = open("PE-txt/p054_poker.txt")		
		for line in file:
			line = line.replace("\n", "")
			hands = line.split(" ")
		
			hand1 = hands[:5]
			hand2 = hands[5:]
			
			if helper(hand1) > helper(hand2):				
				ans +=1 

		return ans

sol = solution()
print(sol.solution0054())
