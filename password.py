import string
import random

// Set chars
chars = string.ascii_letters + string.digits

def createPass():
	
	length = int(input("Şifre Uzunluğu: "))
	
	password = []
	
        // Creating password
	for i in range(length):
		password.append(random.choice(chars))
	
	print("\033[93m" + "".join(password) + "\033[0m")
	

// Run the function	
createPass()
