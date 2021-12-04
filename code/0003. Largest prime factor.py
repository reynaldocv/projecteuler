class solution:
	def solution0003(self, n):
		ans = 1
		while n % 2 == 0: 
			n //= 2
			ans = 2
		
		num = 3
		
		while n > 1:
			print			
			while n % num == 0: 
				n //= num
				ans = num

			num += 2

		return ans 

sol = solution()
print(sol.solution0003(600851475143))
