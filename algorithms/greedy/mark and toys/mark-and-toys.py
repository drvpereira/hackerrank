n, k = map(int, input().split())
prices = sorted(map(int, input().split()))

count = 0
total = 0
for p in prices:
	if total + p <= k:
		count += 1
		total += p
	else:
		break
		
print(count)