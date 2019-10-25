import bisect

n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
bcs = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda bc: bc[1], reverse=True)

for b, c in bcs:
    point = bisect.bisect_left(a, c)

    # print(list())
    for i in reversed(range(max(point-b, 0), point)):

        if a[i] < c:
            a.pop(i)
            # a[i]をcに書き換えたいけどソート順にしたい
            bisect.insort_left(a, c)
        # else:
        #     break
print(sum(a))
