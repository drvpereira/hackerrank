from collections import Counter
s = Counter(Counter(input().strip()).values())
keys, values = list(s.keys()), list(s.values())
print('YES' if not (len(s) > 2 or len(values) > 1 and min(values[0], values[1]) != 1) else 'NO')