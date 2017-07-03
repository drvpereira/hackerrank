input()
list = sorted(map(int, input().strip().split()))
p1, p2, min_diff, pairs = 0, 1, float('inf'), []

while p2 < len(list):
    current_diff = abs(list[p1] - list[p2])
    if current_diff < min_diff:
        min_diff = current_diff
        pairs = list[p1:p2+1]
    elif current_diff == min_diff:
        pairs += list[p1:p2+1]
    p1 += 1
    p2 += 1
    
print(*pairs)