n, d = map(int, input().strip().split())
array = list(map(int, input().strip().split()))
rotated = [ array[(i + d) % n] for i in range(len(array)) ]
print(*rotated)