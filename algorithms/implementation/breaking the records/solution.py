n = int(input().strip())
s = list(map(int, input().strip().split(' ')))

highest, lowest = s[0], s[0]
no_inc, no_dec = 0,0

for i in range(1, len(s)):
    if s[i] > highest:
        highest = s[i]
        no_inc += 1
    elif s[i] < lowest:
        lowest = s[i]
        no_dec += 1

print(no_inc, no_dec)