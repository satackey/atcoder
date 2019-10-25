def calc_replace_count(v):
    nums_count = {}

    for v_i in v:
        if v_i in nums_count:
            nums_count[v_i] += 1
        else:
            nums_count[v_i] = 1

    max_v = max(nums_count.items(), key=lambda x:x[1])

    return len(v) - max_v[1], max_v[0]


n = int(input())
v = list(map(int, input().split()))

v_odd = v[::2]
v_even = v[1::2]

odd_count, odd_key = calc_replace_count(v_odd)
even_count, even_key = calc_replace_count(v_even)

print(len(v) // 2 if odd_key == even_key else odd_count + even_count)
