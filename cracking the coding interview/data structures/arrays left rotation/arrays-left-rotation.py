
def left_rotate(a1, d):
	a2 = [0] * len(a1)

	for i in range(len(a1)):
		a2[i] = a1[(d + i) % len(a1)]

	return a2

n, d = map(int, input().split(' '))
a = list(map(int, input().split(' ')))

print(*left_rotate(a, d))