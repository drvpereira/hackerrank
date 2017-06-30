n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))

positives = sum(i > 0 for i in arr)
negatives = sum(i < 0 for i in arr)
zeroes = sum(i == 0 for i in arr)

total = positives + negatives + zeroes

print('{0:.6f}'.format(positives / total))
print('{0:.6f}'.format(negatives / total))
print('{0:.6f}'.format(zeroes / total))
