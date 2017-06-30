for _ in range(int(input().strip())):
    s = input().strip()
    
    index = 0
    for c in s:
        if c == "hackerrank"[index]:
            index += 1
        if index >= 10:
            break
    print("YES" if index == 10 else "NO")