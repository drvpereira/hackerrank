for _ in range(int(input())):
	s = input()
	changes = sum([ abs(ord(s[k]) - ord(s[len(s) - k - 1])) for k in range(len(s) // 2) ])	
	print(changes)