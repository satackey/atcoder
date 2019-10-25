cube = input()

zero_count = 0
one_count = 0

for i in range(len(cube)):
    if cube[i] == '0':
        zero_count += 1
    else:
        one_count += 1

if zero_count < one_count:
    print(zero_count * 2)
else:
    print(one_count * 2)
