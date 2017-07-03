int(input().strip())
heights = list(map(int, input().strip().split()))
print(heights.count(max(heights)))