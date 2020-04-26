from sys import stderr
from math import ceil

a_takahashi_hp, b_takahashi_attack, c_aoki_hp, c_aoki_attack = map(int, input().split())

takahashi_died_turn_at = ceil(a_takahashi_hp / c_aoki_attack) * 2
aoki_died_turn_at = ceil(c_aoki_hp / b_takahashi_attack) * 2 - 1

print(takahashi_died_turn_at, aoki_died_turn_at, file=stderr)

print('Yes' if takahashi_died_turn_at > aoki_died_turn_at else 'No')
