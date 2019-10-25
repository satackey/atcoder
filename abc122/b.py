s = input()
max_acgt_len = 0

for i in range(len(s)):
    current_str = s[i:]

    for j in reversed(range(1, len(current_str) + 1)):
        acgt_count = 0
        acgt_count += current_str[:j].count('A')
        acgt_count += current_str[:j].count('G')
        acgt_count += current_str[:j].count('C')
        acgt_count += current_str[:j].count('T')

        if acgt_count == len(current_str[:j]):
            max_acgt_len = max(max_acgt_len, acgt_count)

        # print('searching: {}\t\t is acgt: {}'.format(current_str[:j], acgt_count == len(current_str[:j])))
print(max_acgt_len)