from operator import or_
n, m = map(int, input().split())

s = [ list(map(int,input())) for _ in range(n) ]
d = { t: 0 for t in range(m + 1) }

for i in range(len(s)):
	for j in range(i+1, len(s)):
		d[sum(map(or_, s[i], s[j]))] += 1

maxc = max(filter(lambda x: d[x] > 0, d))
print(maxc)
print(d[maxc])