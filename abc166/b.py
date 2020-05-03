
from sys import stderr

def debug(*args):
    print(*args, file=stderr)


def input_sweets_owners():
    input()
    return list(map(int, input().split()))

n_sukuke_num, k_sweets_types_num = map(int, input().split())
ai_sweets_owners = [input_sweets_owners() for _ in range(k_sweets_types_num)]

# debug(ai_sweets_owners)
# for _ in range(k_sweets_types_num):
#     input()
#     ai_sweets_owners.append(list(map(int, input().split())))

sunuke_n_has = {}

for i, sweets_owners in enumerate(ai_sweets_owners):
    for sweets_owner in sweets_owners:
        sunuke_n_has[sweets_owner] = True

# debug(sunuke_n_has)

result = 0
for sunuke_i in range(1, n_sukuke_num+1):
    # debug(sunuke_i in sunuke_n_has)
    if not sunuke_i in sunuke_n_has:
        result += 1

print(result)
