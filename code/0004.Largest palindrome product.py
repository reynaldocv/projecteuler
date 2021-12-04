class solution:
	def solution0004(self, n):
		ans = 0 
		limit = 10**(n - 1)
		for numA in range(10**(n) - 1, 10**(n - 1), -1):			
			if numA < limit:
				return ans
			for numB in range(numA, 10**(n - 1), -1):
				mul = numA*numB
				if str(mul) == str(mul)[::-1]:
					ans = max(ans, mul)
					limit = numB
					break
		return ans
		
sol = solution()
print(sol.solution0004(3))