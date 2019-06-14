#Problem 031 : Coin sums
import datetime

def program():	
	money = 200
	coins = [1, 2, 5, 10, 20, 50, 100, 200]
	ways = [0 for i in range(money + 1)]
	ways[0] = 1

	for coin in coins:
		for i in range(coin, money + 1):
			ways[i] += ways[i - coin]

	return ways[money]
	
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 031 (", h2 - h1, ") : ", ans)

