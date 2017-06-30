grades = [ int(input()) for _ in range(int(input()))]
for grade in grades:
    diff = 5 - (grade % 5)
    if diff <= 2 and grade + diff >= 40:
        print(grade + diff)
    else:
        print(grade)