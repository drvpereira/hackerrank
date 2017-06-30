n = int(input().strip())
no_steps = 1

while no_steps <= n:
    print((' ' * (n - no_steps)) + ('#' * no_steps))
    no_steps += 1