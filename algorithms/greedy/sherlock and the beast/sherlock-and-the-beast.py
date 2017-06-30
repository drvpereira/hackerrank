for _ in range(int(input())):
	n = int(input())
	
	n5 = (n // 3) * 3
	n3 = 0
	r3 = n % 3

	if r3 == 1:
		n5 -= 9
		n3 = 10
	elif r3 == 2:
		n5 -= 3
		n3 = 5

	if n5 < 0 or n3 < 0:
		print('-1')
	else:
		print('5' * n5 + '3' * n3)
		