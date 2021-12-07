from collections import defaultdict

class solution:
    def solution0061(self):
        def helper(arr, mask):
            nonlocal ans
            if len(arr) == 6: 
                if arr[-1] % 100 == arr[0] // 100:
                    ans = sum(arr)
            else: 
                for i in range(4, 9):
                    if (mask & 1 << i) >> i == 0: 
                        for num in numbers[i]: 
                            if arr[-1] % 100 == num // 100:
                                arr.append(num)
                                helper(arr, mask ^ 1 << i)
                                arr.pop()

        numbers = defaultdict(lambda: []) 

        for i in range(20, 143):
            num = i*(i + 1)//2
            if len(str(num))== 4:
                numbers[3].append(num)
            num = i**2
            if len(str(num))== 4:            
                numbers[4].append(num)
            num = i*(3*i - 1)//2
            if len(str(num))== 4:            
                numbers[5].append(num)
            num = i*(2*i - 1)
            if len(str(num))== 4:            
                numbers[6].append(num)
            num = i*(5*i - 3)//2            
            if len(str(num))== 4:            
                numbers[7].append(num)
            num = i*(3*i - 2)            
            if len(str(num))== 4:            
                numbers[8].append(num)

        ans = 0 
        for num in numbers[3]:
            helper([num], 1<<3)

        return ans



sol = solution()
print(sol.solution0061())