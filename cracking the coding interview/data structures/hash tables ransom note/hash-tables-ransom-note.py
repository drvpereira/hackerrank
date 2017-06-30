
def hist(text):
	h = dict(zip(text, [0] * len(text)))
	for word in text:
		h[word] += 1
	return h

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
note = input().strip().split(' ')

hm = hist(magazine)
hn = hist(note)

possible = True
for word in note:
	if hn[word] > hm[word]:
		possible = False

if(possible):
    print("Yes")
else:
    print("No")