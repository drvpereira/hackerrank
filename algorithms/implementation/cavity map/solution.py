def is_cavity(i, j):
	for k in [-1, 1]:
		if area[i+k][j] >= area[i][j] or area[i][j+k] >= area[i][j]:
			return False
	return True

n = int(input())
area = [ list(input()) for _ in range(n) ]
output = [ list(l) for l in area ]

for i in range(1, n-1):
	for j in range(1, n-1):
		if is_cavity(i, j):
			output[i][j] = 'X'

print('\n'.join(''.join(l) for l in output))