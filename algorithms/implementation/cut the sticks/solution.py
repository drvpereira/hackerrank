int(input())
sticks = list(map(int, input().split()))

while sticks:
    print(len(sticks))
    cut = min(sticks)
    sticks = [ i-cut for i in sticks if i-cut > 0 ]
