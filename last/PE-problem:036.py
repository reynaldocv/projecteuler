#Problem 036 : Double-base palindromes
import datetime

def program():	
	palindromes = []
	for nro in range(1,1000):
		str_nro = str(nro)
		palindromes.append(int(str_nro + str_nro[::-1]))
		palindromes.append(int(str_nro + str_nro[::-1][1:]))
	
	ans = 0	
	for nro in palindromes: 
		str_bin = str(bin(nro))[2:]
		if str_bin == str_bin[::-1]:
			ans += nro
	
	return ans

if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 036 (", h2 - h1, ") : ", ans)

