n = int(input())

sum_yen = 0.0

for i in range(n):
    x, u = input().split()

    if u == 'JPY':
        sum_yen += int(x)
    else:
        sum_yen += float(x) * 380000.0

print(sum_yen)
