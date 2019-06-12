import os
from pathlib import Path

def program():
	for i in range(1,10):		
		file = "PE-problem:00"+str(i)+".py"		
		my_file = Path(file)
		if my_file.is_file():
			os.system("python3 "+file)

	for i in range(10,100):		
		file = "PE-problem:0"+str(i)+".py"		
		my_file = Path(file)
		if my_file.is_file():
			os.system("python3 "+file)

if __name__ == "__main__":
	program()

