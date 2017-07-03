from math import sqrt

for _ in range(int(input())):
	a, b = map(int, input().split())

	na, nb = int(sqrt(a)), int(sqrt(b))
	sqs = nb - na
	
	if sqrt(a) == na:
		sqs += 1

	print(sqs)