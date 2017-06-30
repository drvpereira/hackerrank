from math import floor, sqrt

def power_sum(x, i, n):
	if x < 0:
		return 0

	if x == 0:
		return 1

	result = 0
	for i in range(i+1, floor(sqrt(x))+1):
		result += power_sum(x - pow(i, n), i, n)
	return result

x, n = int(input()), int(input())

print(power_sum(x, 0, n))