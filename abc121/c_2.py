n, m = map(int, input().split())
a = []
purchase_price = 0
collected = []
collected_count = 0

for i in range(n):
    a.append(list(map(int, input().split())))
    if collected_count + a[i][1] <= m:
        collected_count += a[i][1]
        collected.append(a[i])
    else:
        for j in len(collected):
        # for price, count in collected_count:
            # 今の店の方が安いとき
            if collected[j][0] > a[i][0]:
                # 全て置き換えられる時
                if collected[j][1] <= a[i][1]:
                    collected[j][0] = a[i][0]
                else:
                    collected[j][1] -= a[i][1]
                    collected.append()
print(purchase_price)
