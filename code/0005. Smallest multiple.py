from math import gcd

class solution:
    def solution0005(self, n):
        ans = 1
        for i in range(2, n + 1):
            aux = gcd(ans, i)
            ans = i*ans // aux
        
        return ans

sol = solution()
print(sol.solution0005(20))
    