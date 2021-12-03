class solution:
	def solution0001(self, n): 
		ans = 0

    for num in range(3, n):
			if num % 3 == 0 or num % 5 == 0: 
				ans += num

		return ans

sol = solution()
print(sol.solution0001(1000))
