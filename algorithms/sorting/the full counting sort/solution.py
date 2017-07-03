n = int(input())
count = [0] * 100
x = []

for i in range(n):
	l = input().split()
	if i < n // 2:
		x.append( (int(l[0]), '-') )
	else:
		x.append( (int(l[0]), l[1]) )

for i in x:
	count[i[0]] += 1

for i in range(1, len(count)):
	count[i] += count[i-1]

sorted = [0] * len(x)
for i in range(len(x)-1, -1, -1):
	sorted[count[x[i][0]]-1] = x[i] #29
	count[x[i][0]] -= 1

print(' '.join(map(lambda x: str(x[1]), sorted)))