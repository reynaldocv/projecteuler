
import datetime
from collections import defaultdict

class solution():
    def solution0051(self, k):
        def genKeys(num):
            strNum = [char for char in str(num)]
            n = len(strNum)
            ans = []
            for num in range(1, 2**n):
                aux = num
                var = ""
                prev = None
                for i in range(n):
                    if aux & 1 == 1:
                        prev = strNum[i] if prev == None else prev
                        if prev != strNum[i]:
                            break
                        var += "*"
                    else:
                        var +=  strNum[i]
                    aux >>= 1
                if len(var) == n: 
                    ans.append(var)
            
            return ans
                
        def isPrime(num):
            limit = int(num**.5) + 2
            for prime in primes: 
                if prime <= limit: 
                    if num % prime == 0: 
                        return False
            
            return True

        primes = [2, 3, 5, 7]
        num = 11
        seen = defaultdict(lambda: [])
        while True: 
            if isPrime(num):
                for key in genKeys(num):
                    seen[key].append(num)
                    if len(seen[key]) >= k:
                        return min(seen[key])
            
                primes.append(num)

            num += 2

sol = solution()
h1 = datetime.datetime.now()	

print(sol.solution0051(8))
h2 = datetime.datetime.now()	
print("Problem 001 (",h2 - h1,") : ")




