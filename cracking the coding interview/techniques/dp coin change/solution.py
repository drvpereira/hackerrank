
def coin_change(n, c):
	change = [0] * (n + 1)
	change[0] = 1

	for v in c:
		for i in range(v, n+1):
			change[i] += change[i - v] 

	return change[-1]


n, m = map(int, input().split(' '))
c = list(map(int, input().split(' ')))

print(coin_change(n, c))