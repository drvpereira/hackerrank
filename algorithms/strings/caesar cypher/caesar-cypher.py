n = int(input().strip())
s = input().strip()
k = int(input().strip())

encoded = ""
for c in s:
    if c >= 'A' and c <= 'Z':
        encoded += chr( (ord(c) - 65 + k) % 26 + 65 )
    elif c >= 'a' and c <= 'z':
        encoded += chr( (ord(c) - 97 + k) % 26 + 97 )
    else:
        encoded += c
        
print(encoded)