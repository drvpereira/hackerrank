from string import ascii_lowercase

s = input().lower()
d = { c : 0 for c in ascii_lowercase + ' ' }

for c in s:
    d[c] += 1

print("pangram" if len(list(filter(lambda x: x == 0, d.values()))) == 0 else "not pangram")