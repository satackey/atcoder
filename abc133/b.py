from math import sqrt

n, d = map(int, input().split())
x_s = [list(map(int, input().split())) for _ in range(n)]

def calc_dist(y_s, z_s):
    yz_s = [[y_s[i], z_s[i]] for i in range(d)]

    distance = 0
    for y, z in yz_s:
        distance += abs(y - z) ** 2
    distance = sqrt(distance)
    return distance

cnt = 0
for i in range(n):
    for j in range(i+1, n):
        dist = calc_dist(x_s[i], x_s[j])
        if dist % 1 == 0:
            cnt += 1

print(cnt)