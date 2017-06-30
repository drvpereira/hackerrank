for _ in range(int(input())):
    m = int(input())
    n = int(input())
    costs = list(map(int, input().split()))
    
    visited = {}
    for i in range(len(costs)):
        if m - costs[i] in visited:
            print(visited[m - costs[i]], i + 1)
            break
        else:
            visited[costs[i]] = i + 1