def coin_change(n, coins):
	memo = [ 0 if j > 0 else 1 for j in range(n+1)]
	for i in range(len(coins)):
		for j in range(1, n+1):
			if j >= coins[i]:
				memo[j] += memo[j - coins[i]]
	return memo[n]

n, m = map(int, input().strip().split(' '))
c = list(map(int, input().strip().split(' ')))
print(coin_change(n, c))
