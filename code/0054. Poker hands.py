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
						return (9,) + tuple(sorted(numbers.keys(), reverse = True))
					else: 
						return (5,) + tuple(sorted(numbers.keys(), reverse = True))
				
				elif sorted(numbers.keys()) == [2,3,4,5,14]:
					if len(types) == 1: 
						return (9, 5, 4, 3, 2, 1)
					else: 
						return (5, 5, 4, 3, 2, 1)

				elif len(types) == 1: 
					return (6,) + tuple(sorted(numbers.keys(), reverse = True))		
				else: 
					return (1,) + tuple(sorted(numbers.keys(), reverse = True))
				
			elif len(numbers) == 4: 
				return (2,) + tuple([key for key in numbers if numbers[key]== 2]*2) + tuple(sorted([key for key in numbers if numbers[key]== 1], reverse = True))
			elif len(numbers) == 3:
				if max(numbers.values()) == 3: 
					return (4,) + tuple([key for key in numbers if numbers[key]== 3]*3) + tuple(sorted([key for key in numbers if numbers[key]== 1], reverse = True))
				else:
					return (3,) + tuple(sorted([key for key in numbers if numbers[key]== 2]*2, reverse = True)) + tuple([key for key in numbers if numbers[key]== 1])
			elif len(numbers) == 2: 
				if max(numbers.values()) == 4: 
					return (8,) + tuple(sorted([key for key in numbers if numbers[key] == 4]*4)) + tuple(sorted([key for key in numbers if numbers[key] == 1]))
				else: 
					return (7,) + tuple(sorted([key for key in numbers if numbers[key] == 3]*3)) + tuple(sorted([key for key in numbers if numbers[key] == 2]*2))
				
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
			if helper(hand1)[0] == 9 or helper(hand2)[0] == 9:
				print(hand1, helper(hand1))
				print(hand2, helper(hand2))

			if helper(hand1) > helper(hand2):
				
				ans +=1 

		return ans

sol = solution()
print(sol.solution0054())
