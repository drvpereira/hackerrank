for _ in range(int(input())):
	money = int(input())
	n = int(input())
	costs = list(map(int, input().split(' ')))

	for i1 in range(len(costs)):
		for i2 in range(i1+1, len(costs)):
			if costs[i1] + costs[i2] == money:
				print(i1+1, i2+1)


