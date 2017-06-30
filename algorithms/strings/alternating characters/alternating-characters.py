t = int(input())

for _ in range(t):
	s = input()
	
	ndel = 0
	for i in range(1,len(s)):
		if s[i] == s[i-1]:
			ndel += 1
	
	print(ndel)