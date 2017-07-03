
def pairs(a,k):
    result = 0
    visited = {}
    for v in a:
        if (v + k) in visited:
            result += 1
        if (v - k) in visited:
            result += 1
        visited[v] = 1
    return result

n, k = map(int, input().strip().split())
a = list(map(int, input().strip().split(' ')))
print(pairs(a, k))
