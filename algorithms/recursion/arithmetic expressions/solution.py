solution = []

def operate(n1, n2, op):
	if op == '+':
		return n1 + n2
	elif op == '-':
		return n1 - n2
	else:
		return n1 * n2

def find_expression(numbers, total, ops = []):
	if len(solution) == 0:
		if len(numbers) >= 2 and numbers[0] % 101 != 0:
			for op in [ '+', '-', '*' ]:
				find_expression([ operate(numbers[0], numbers[1], op) ] + numbers[2:], total, ops + [op])
		else:
			if numbers[0] % 101 == 0:
				while len(ops) < total:
					ops.append('*')
				solution.append(ops)


n = int(input())
numbers = list(map(int, input().split(' ')))
find_expression(numbers, len(numbers) - 1)

i = 0
for n in numbers:
	print(n, end='')
	if i < len(solution[0]):
		print(solution[0][i], end='')
		i += 1
print