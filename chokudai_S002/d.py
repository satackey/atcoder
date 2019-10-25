coins = sorted([''.join(sorted(input().split())) for _ in range(int(input()))])

count = 0
last_coin = ''
for coin in coins:
    if last_coin != coin:
        count += 1
    last_coin = coin
print(count)