n = int(input().strip())
b = input().strip()

index = b.find('010')
count = 0

while index != -1:
    b = b[:index+2] + '1' + b[index+3:]
    index = b.find('010')
    count += 1
    
print(count)