for _ in range(int(input().strip())):
    s = input().strip()
    beautiful = False
    for i in range(1, (len(s) // 2) + 1):
        first_number = int(s[:i])
        number = first_number
        string = str(number)
        while len(string) < len(s):
            number += 1
            string += str(number)
        if string == s:
            beautiful = True
            break
    print('YES ' + str(first_number) if beautiful else 'NO')