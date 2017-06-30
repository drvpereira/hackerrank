s = input()
d = { c: s.count(c) for c in set(s) if s.count(c) % 2 == 1 }
print("YES" if len(d) <= 1 else "NO")