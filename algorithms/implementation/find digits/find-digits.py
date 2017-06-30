
for _ in range(int(input())):
	n = input()
	count = sum(int(l) != 0 and int(n) % int(l) == 0 for l in n)
	print(count)