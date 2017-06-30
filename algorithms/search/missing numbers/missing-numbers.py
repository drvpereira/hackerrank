def build_hist(array):
    hist = {}
    for v in array:
        if v not in hist:
            hist[v] = 1
        else:
            hist[v] += 1
    return hist
        
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

hist_a, hist_b = build_hist(a), build_hist(b)

result = []
for key in hist_b:
    if key not in hist_a or hist_a[key] != hist_b[key]:
        result.append(str(key))

print(*result)