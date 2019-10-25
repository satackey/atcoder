a500 = int(input())
b100 = int(input())
c50 = int(input())

x = int(input())

count = 0
last_500_number = 0
last_100_number = 0
last_50_number = 0

while True:
    x_remainder = x

    last_500_number = (a500 - x_remainder % 500) / 500
    last_100_number = (b100 - x )

    # if hoge:
    #     count += 1
    # else:
    #     break;
    break

# 1050 500 3 -> 2, 50
# 1550, 500, 2 -> 1, 550
def count_coin(amount, coin, max):
    remainder = amount % coin
    coin_count = amount // coin

    if coin_count > max:
        coin_count = max

    return [coin_count, remainder]
print('a')
amount, coin, max = map(int, input().split())
print('b')
print(count_coin(amount, coin, max))


