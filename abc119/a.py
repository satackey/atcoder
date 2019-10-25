y, m, d = map(int, input().split('/'))

if y < 2019 or y == 2019 and (m < 4 or m == 4 and d < 31):
    print('Heisei')
else:
    print('TBD')
