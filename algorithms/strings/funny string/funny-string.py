
def funny_string(s):
    n = len(s)
    funny = True
    for i in range(1, n):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(s[n-i]) - ord(s[n-i-1])):
            funny = False
            break
    return "Funny" if funny else "Not Funny"

for _ in range(int(input().strip())):
    s = input().strip()
    print(funny_string(s))
