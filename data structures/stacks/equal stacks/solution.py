from collections import deque

n1, n2, n3 = map(int, input().strip().split(' '))

s1 = deque(map(int, input().strip().split(' ')))
s2 = deque(map(int, input().strip().split(' ')))
s3 = deque(map(int, input().strip().split(' ')))

h1 = sum(s1)
h2 = sum(s2)
h3 = sum(s3)

while h1 != h2 or h2 != h3:
    max_height = max(h1, h2, h3)
    
    if h1 == max_height:
        h1 -= s1.popleft()
    elif h2 == max_height:
        h2 -= s2.popleft()
    else:
        h3 -= s3.popleft()

print(h1)