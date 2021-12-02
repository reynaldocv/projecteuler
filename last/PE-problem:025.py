#Problem 025 : 1000-digit Fibonacci number
import datetime

def program():	
	f1 = f2 = 1 
	i_th = 2
	while len(str(f1)) < 1000:
		i_th += 1
		aux = f1
		f1 += f2
		f2 = aux
		
	return i_th	
	
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 025 (", h2 - h1, ") : ", ans)

