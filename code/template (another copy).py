class solution:
    def solution0094(self, n):
        limit = int((n*2)**.5) + 10
        ans = 0 
        for l in range(1, limit):
            h = (l**2 - ((l + l)/2)**2)**.5
            if 0 < h*(l + 1) <= n: 
                ans += 3*l + 1

        for l in range(2, limit):
            h = (l**2 - ((l - l)/2)**2)**.5
            if 0 < h*(l - 1) <= n: 
                ans += 3*l - 1

        return ans

sol = solution()
print(sol.solution0094(10**9))

