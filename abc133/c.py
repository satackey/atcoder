from math import floor, ceil

l, r = map(int, input().split())

# x から y までの中でもっとも2019の倍数に近いもの
def hoge(x, y):
    min_index = floor(x / 2019)
    max_index = ceil(y / 2019)

    if max_index - min_index > 1:
        return 2019 * min_index
    else:
        min_ = min(x, (min_index+1) * 2019)
        max_ = max(y, (max_index-1) * 2019)
        pass


# hoge_min = l // 2019
# hoge_max = r // 2019
#
# i_min = max(hoge_min * 2019, l)
# i_max = min((hoge_min + 1) * 2019, r-1)
# i_mod1 = i_min - hoge_min * 2019
# i_mod2 = (hoge_min + 1) * 2019 - i_max
# i_mod = min(i_mod1, i_mod2) + hoge_min * 2019
#
# j_min = max(hoge_max * 2019, i_mod+1)
# j_max = min((hoge_max + 1) * 2019, r)
# j_mod1 = j_min - hoge_max * 2019
# j_mod2 = (hoge_max + 1) * 2019 - j_max
# j_mod = min(j_mod1, j_mod2) + hoge_max * 2019
#
# ans = i_mod * j_mod % 2019

hoge(l, r)
# print(ans)
