from collections import Counter

for _ in range(int(input().strip())):
    s1 = Counter(input().strip())
    s2 = Counter(input().strip())
    print('YES' if len((s1 - s2).values()) < len(s1) else 'NO')