from collections import Counter

def anagram(s):
    s1 = s[:len(s)//2]
    s2 = s[len(s)//2:]
    if len(s1) != len(s2):
        return -1
    else:
        return sum((Counter(s1)-Counter(s2)).values())

for _ in range(int(input().strip())):
    s = input().strip()
    print(anagram(s))
