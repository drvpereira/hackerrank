from math import floor, sqrt

def is_prime(n):
	if n == 2:
		return True
	elif n == 1 or n % 2 == 0:
		return False

	for x in range(3, floor(sqrt(n))+1, 2):
		if n % x  == 0:
			return False

	return True

for _ in range(int(input())):
	if (is_prime(int(input()))):
		print('Prime')
	else:
		print('Not prime')