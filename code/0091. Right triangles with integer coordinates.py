from math import gcd

class solution: 
	def solution0091(self, n):
		ans = 3*n**2
		
		print(ans)
		for i in range(1, n + 1):		
			for j in range(1, n + 1):
				times = 1
				fator = gcd(i, j)
				while 0 <= i + times*(j//fator) <= n and 0 <= j - times*(i//fator) <= n:
					ans += 1
					times += 1
				
				times = 1
				while 0 <= i - times*(j//fator) <= n and 0 <= j + times*(i//fator) <= n:
					ans += 1
					times += 1
		
		return ans

sol = solution()

print(sol.solution0091(50)) 
