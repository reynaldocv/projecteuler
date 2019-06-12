#Problem 018: Maximum path sum I
import datetime

def program():	
	archivo = open('PE-problem 022_names.txt')
	nombres = []
	for line in archivo:
		line = line.replace('"','')
		nombres = line.split(',')
		
	nombres.sort()
	rpta=0
	

if __name__ == "__main__":
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 018 (",h2 - h1,") : ", ans)

