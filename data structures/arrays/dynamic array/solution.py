n, q = map(int, input().strip().split())
seq_list = [ [] for _ in range(n) ]
last_answer = 0

for _ in range(q):
    t, x, y = map(int, input().strip().split())
    if t == 1:
        seq_list[(x ^ last_answer) % n].append(y)
    else:
        seq = seq_list[(x ^ last_answer) % n]
        last_answer = seq[y % len(seq)]
        print(last_answer)