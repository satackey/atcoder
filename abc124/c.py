ss = input()

first_zero_count = 0
first_zero_last = '0'
first_one_count = 0
first_one_last = '1'
for s in ss:
    first_zero_count += 1 if s == first_zero_last else 0
    first_one_count += 1 if s == first_one_last else 0
    first_zero_last, first_one_last = first_one_last, first_zero_last
print(min(first_zero_count, first_one_count))
