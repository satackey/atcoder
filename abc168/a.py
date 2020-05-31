n = int(input())

n_1nokurai = n % 10

hon = [2, 4, 5, 7, 9]
pon = [0, 1, 6, 8]
bon = [3]

if n_1nokurai in hon:
    print('hon')
elif n_1nokurai in pon:
    print('pon')
elif n_1nokurai in bon:
    print('bon')
