store_num, order_num = map(int, input().split())

stores = []
for store_i in range(store_num):
    price, stocks_num = map(int, input().split())
    stores.append({
        'price': price,
        'stocks_num': stocks_num
    })

buyed = []
buyed_sum = 0

for store_i in range(store_num):
    if buyed_sum + stores[store_i]['stocks_num'] < order_num:  # この店の全ての本数を買う時
        # 購入済みの list に追加
        buyed.append({
            'price': stores[store_i]['price'],
            'num': stores[store_i]['stocks_num']
        })
        # 購入済みの本数を増やす
        buyed_sum += stores[store_i]['stocks_num']
        # この店の在庫を減らす
        stores[store_i]['stocks_num'] = 0

    elif buyed_sum < order_num:  # この店で一部の本数を買う時(全て買うと多すぎる)
        buy_num = order_num - buyed_sum
        # 購入済みの list に追加
        buyed.append({
            'price': stores[store_i]['price'],
            'num': buy_num
        })
        # 購入済みの本数を増やす
        buyed_sum += buy_num
        # この店の在庫を減らす
        stores[store_i]['stocks_num'] -= buy_num

    # まだ在庫が存在するなら
    if stores[store_i]['stocks_num'] > 0:
        for buyed_i in range(len(buyed)):
            if buyed[buyed_i]['price'] > stores[store_i]['price']:  # 今までの店の価格より,今の店の価格が安ければ
                buy_num = min(buyed[buyed_i]['num'], stores[store_i]['stocks_num'])
                # 新しく買った本数を前に買った店から減らす
                buyed[buyed_i]['num'] -= buy_num

                # 購入済みの list に追加
                buyed.append({
                    'price': stores[store_i]['price'],
                    'num': buy_num
                })
buyed
print(sum(buy['price'] * buy['num'] for buy in buyed))
