for _ in range(int(input())):
	n = int(input())
	h = 1
	
	for i in range(n):
		if i % 2 == 0:
			h *= 2
		else:
			h += 1
			
	print(h)