
def stair(size):
	s0, s1, s2 = 1, 1, 2

	for i in range(size):
		s0, s1, s2 = s1, s2, s0+s1+s2
	return s0

s = int(input())
for _ in range(s):
    n = int(input())
    print(stair(n))