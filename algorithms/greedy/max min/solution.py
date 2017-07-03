n = int(input())
k = int(input())

packages = sorted(int(input()) for _ in range(n))
unfairness = min(packages[i+k-1] - packages[i] for i in range(len(packages)-k+1))

print(unfairness)