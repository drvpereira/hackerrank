def is_leap(year):
    if year < 1918:
        return year % 4 == 0
    else:
        return year % 400 == 0 or year % 4 == 0 and year % 100 != 0

def solve(year):
    first_8 = 243
    if year == 1918:
        first_8 -= 13
    if is_leap(year):
        first_8 += 1
    day = str(256 - first_8)
    if len(day) < 2:
        day = '0' + day
    return day + '.09.' + str(year)
    

year = int(input().strip())
result = solve(year)
print(result)
