n, q = map(int, input().split())
s = input()
questions = [list(map(int, input().split())) for _ in range(q)]

ac_sum = [0]
for i in range(1, n + 1):
    ac_sum.append(ac_sum[i-1] + 1 if s[i-1 : i+1] == 'AC' else ac_sum[i-1])

for l, r in questions:
    print(ac_sum[r-1] - ac_sum[l-1])
