import math

x_goal = int(input())

# print(math.ceil(math.log(x_goal / 100, 1.01)))
result = 0
balance = 100
while balance < x_goal:
    balance = (balance * 1.01) // 1
    result += 1

print(result)