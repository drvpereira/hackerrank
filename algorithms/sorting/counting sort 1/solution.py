input()
ar = map(int, input().strip().split())
count = [0] * 100

for i in ar:
	count[i] += 1

print(*count)