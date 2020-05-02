import sys

k_goal = int(input())
a_current_min, b_current_max = map(int, input().split())

for i in range(a_current_min, b_current_max + 1):
    if i % k_goal == 0:
        print('OK')
        sys.exit(0)

print('NG')
