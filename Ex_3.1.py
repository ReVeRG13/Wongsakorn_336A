def Odd(L, R):
	if (R < L):
		return
    
	if (R % 2 == 1):
		Odd(L, R - 2)
	else:
		Odd(L, R - 1)
	if (R % 2 == 1):
		print(R, end = " ")
    
def Even(L, R):
	
	# Base case
	if (R < L):
		return

	if (R % 2 == 0):
		Even(L, R - 2)
	else:
		Even(L, R - 1)

	if (R % 2 == 0):
		print(R, end = " ")

if __name__ == '__main__':

	L = eval(input("add L : "))
	R = eval(input("add R : "))
	
	print("Odd numbers:")
	Odd(L, R)
	print()

	print("Even numbers:")
	Even(L, R)
