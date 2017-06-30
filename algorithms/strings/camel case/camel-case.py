s = input().strip()
total = 1
for c in s:
    if c.isupper():
        total += 1
print(total)