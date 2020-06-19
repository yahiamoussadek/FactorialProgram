# this is my first program ever in python 



def factorial(n):
	if n == 0 or n == 1:
		return 1
	elif n < 0 :
		return -1
	else : 
		fact = n * factorial(n - 1)
		return fact

x = int(input("Please enter an integer: "))
print(factorial(x))			
			 