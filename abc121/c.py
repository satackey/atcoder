n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

def bubble_sort(lst):
    for i in reversed(range(len(lst))):
        for j in range(i):
            if lst[j][0] > lst[j + 1][0]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

bubble_sort(a)
purchase_price = 0

for price, count in a:
    if count < m:
        purchase_price += price * count
        m -= count

    else:
        purchase_price += price * m
        m = 0

print(purchase_price)
