input()
ar = list(map(int, input().strip().split()))
count = [0] * 100

for i in ar:
	count[i] += 1

j = 0
for idx, val in enumerate(count):
	for k in range(val):
		ar[j] = idx
		j += 1

print(*ar)