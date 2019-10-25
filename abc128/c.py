n, m = map(int, input().split())
kss_ = [list(map(int, input().split())) for _ in range(m)]
kss = list(map(lambda ks: [ks[0], ks[1:]], kss_))
p = map(int, input().split())
