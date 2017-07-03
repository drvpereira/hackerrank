def solve(a, b):
    diff = [ i - j for i, j in zip(a,b) ]
    alice = sum(i > 0 for i in diff)
    bob = sum(i < 0 for i in diff)
    return (alice, bob)

a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
result = solve(a, b)
print(*result)
