s = input().strip()
count = 0
for i in range(len(s)):
    if s[i] != "SOS"[i % 3]:
        count += 1
print(count)