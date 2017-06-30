
for _ in range(int(input())):
	n, a, b = int(input()), int(input()), int(input())	
	mn, mx = min(a,b) * (n-1), max(a,b) * (n-1)

	v = [ mn ]
	while v[-1] < mx:
		v.append(v[-1] + abs(b-a))
	
	print(*v)