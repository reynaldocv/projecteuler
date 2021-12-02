#Problem 037 : Truncatable primes
import datetime

def program():	
	def is_prime(nro):
		if nro <= 1: return False
		if nro == 2: return True
		lim = int(nro**(.5)) + 1
		if nro % 2 == 0:
			return False
		else:
			for i in range(3, lim, 2):
				if nro % i == 0:
					return False
			return True
	
	ans = set([])
	nros = [3, 7]
	while len(ans) < 11:
		new_nros = []
		for nro in nros: 
			for dig in [1, 2, 3, 5, 7, 9]:
				new_nro = aux = int(str(dig) + str(nro))	
				if is_prime(new_nro):							
					truncatable = True
					while aux > 0:
						if not is_prime(aux):
							truncatable = False
							aux = 0
						aux //= 10
					if truncatable: 
						ans.add(new_nro)
					new_nros.append(new_nro)
		nros = new_nros
	
	ans = sorted(ans)
	return sum(ans[:11])
					
						
			
					
		


	
if __name__ == "__main__":	
	h1 = datetime.datetime.now()
	ans = program()
	h2 = datetime.datetime.now()
	print("Problem 035 (", h2 - h1, ") : ", ans)

					

