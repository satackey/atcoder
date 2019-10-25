n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

a = sorted(a, key=lambda x: x[0])
purchase_price = 0


for price, count in a:
    if count < m:
        purchase_price += price * count
        m -= count

    else:
        purchase_price += price * m
        m = 0

print(purchase_price)
