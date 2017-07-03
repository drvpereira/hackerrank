s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split())
apples = list(map(int, input().split()))
oranges = list(map(int, input().split()))

total_apples = 0
for apple in apples:
    if a + apple >= s and a + apple <= t:
        total_apples += 1
print(total_apples)

total_oranges = 0
for orange in oranges:
    if b + orange >= s and b + orange <= t:
        total_oranges += 1
print(total_oranges)