# Write your solution for 1.4 here!

def is_prime(x):
	num = int (x)
	for i in range (2, num):
		if i!=num-1:
			if num% i == 0:
				print("not prime!!!")
				return("not prime!!!")
		else:
			if num% i == 0:
				print("not prime!!!")
				return("not prime!!!")
			else:
				print("its a prime!!!")
				return("its a prime!!")

	pass
a = is_prime(101)