
n = int(input())
heights = list(map(int, input().strip().split()))
heights.append(0)

stack = []
max_size = 0

for height in heights:
	pos = 0
	while len(stack) > 0 and stack[-1] > height:
		pos += 1
		max_size = max(max_size, pos * stack.pop())
	for j in range(pos+1):
		stack.append(height)

print(max_size)