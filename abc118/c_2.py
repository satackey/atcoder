n = int(input())
a = list(map(int, input().split()))


def bubble_sort(lst):
    for i in reversed(range(len(lst))):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def attack_monsters(monster1, monster2):
    if monster1 > monster2:
        result = monster1 % monster2
    else:
        result = monster2 % monster1

    return result if result != 0 else min(monster1, monster2)


# bubble_sort(a)
min_monster = a[0]
for i in range(1, n):
    if a[i] == 0:
        continue

    result = attack_monsters(min_monster, a[i])
    min_monster = attack_monsters(result, min_monster)


print(min_monster)