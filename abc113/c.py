pref_num, city_num = map(int, input().split())
py = sorted([list(map(int, input().split())) + [i] for i in range(city_num)], key=lambda py: py[1])

city_num_in_prefs = [0 for _ in range(pref_num)]

city_nums = []
for pref, year, i in py:
    city_num_in_prefs[pref-1] += 1
    city_num = "{:06}{:06}".format(pref, city_num_in_prefs[pref-1])
    city_nums.append([city_num, i])

city_nums.sort(key=lambda x: x[1])
for num, index in city_nums:
    print(num)
