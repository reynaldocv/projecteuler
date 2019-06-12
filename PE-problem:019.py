#Problem 019: Counting Sundays
import datetime

def program():	
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	day = 1 + 365
	ans = 0
	for year in range(1901, 2001):
		for month in range(12):
			day += days[month]
			if month == 1:
				if year % 400 or year % 4 == 0:
					day += 1
			if day % 7 == 0:
				ans += 1
	return ans	

if __name__ == "__main__":
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 019 (", h2 - h1, ") : ", ans)

