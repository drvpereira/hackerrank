
def super_digit(n):
	if len(n) == 1:
		return n
	return super_digit(str(sum(map(int, list(n)))))

n, k = map(int, input().split(' '))

print(super_digit(super_digit(str(n)) * k))