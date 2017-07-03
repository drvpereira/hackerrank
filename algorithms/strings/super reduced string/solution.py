
def reduce(s):
    i = 0
    reduced = ''
    while i < len(s):
        if i < (len(s) - 1) and s[i] == s[i+1]:
            i += 2
        else:
            reduced += s[i]
            i += 1
    return reduced            

s = input().strip()
reduced = reduce(s)

while reduced != s:
    s = reduced
    reduced = reduce(s)

if reduced: 
    print(reduced)
else:
    print('Empty String')