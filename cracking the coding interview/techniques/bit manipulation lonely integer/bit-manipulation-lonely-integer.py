def lonely_integer(a):
	h = [0] * 101

	for i in a:
		h[i-1] += 1
	
	for i in range(len(h)):
		if h[i] == 1:
			return i+1
	
	return 0

n = int(input())
a = list(map(int, input().split(' ')))
print(lonely_integer(a))