n = int(input())

sps = []
for i in range(n):
    s, p = input().split()
    p = int(p)
    sps.append({
        "city": s,
        "score": p,
        "index": i
    })
# sps.sort()

cities = {}
for sp in sps:
    if not sp["city"] in cities:
        cities[sp["city"]] = []
    cities[sp["city"]].append(sp)

# [v.sort() for k, v in cities.items()]
rest_sorted_cities = {}
for k, v in cities.items():
    rest_sorted_cities[k] = sorted(v, key=lambda x:x["score"], reverse=True)

sorted_cities = sorted(rest_sorted_cities.items(), key=lambda x: x[0])

for k, city in sorted_cities:
    [print(rest["index"] + 1) for rest in city]
