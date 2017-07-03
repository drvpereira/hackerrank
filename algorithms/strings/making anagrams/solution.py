from collections import Counter
c1 = Counter(input().strip())
c2 = Counter(input().strip())
print(sum(((c1 - c2) + (c2 - c1)).values()))
