from functools import cache

class solution: 
	def solution0002(self, n):
		@cache
		def fibonacci(x):
			if x <= 1: 
				return 1
			else: 
				return fibonacci(x - 2) + fibonacci(x - 1)

		ans = 0
		ith = 1
		while fibonacci(ith) < n: 
			if fibonacci(ith) % 2 == 0: 
				ans += fibonacci(ith)
			ith += 1

		return ans

sol = solution()
print(sol.solution0002(4*10**6))
	
