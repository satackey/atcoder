n = int(input())
a = list(map(int, input().split()))


def bubble_sort(lst):
    for i in reversed(range(len(lst))):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

bubble_sort(a)
zero_monster_indexes = []

while True:
    for monster_i in range(1, len(a)):
        if a[monster_i] == 0:
            zero_monster_indexes.append(monster_i)
        else:
            a[monster_i] %= a[0]

            if a[monster_i] == 0:
                zero_monster_indexes.append(monster_i)

    for zero_monster_index in reversed(zero_monster_indexes):
        a.pop(zero_monster_index)
    zero_monster_indexes.clear()

    bubble_sort(a)

    if len(a) == 1:
        break

print(a[0])
