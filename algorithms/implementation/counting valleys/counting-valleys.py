n = int(input().strip())
steps = input().strip()

valleys, current_level = 0, 0

for step in steps:
    if step == 'D':
        current_level -= 1
    else:
        current_level += 1
        if current_level == 0:
            valleys += 1
        
print(valleys)