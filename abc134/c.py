n = int(input())
a_s_with_index = [(i, int(input())) for i in range(n)]
a_s = [a_i[1] for a_i in a_s_with_index]
a_s.sort()

for i, a_i in a_s_with_index:
    if  a_i == a_s[n-1]:
        a_max_i = n-2
    else:
        a_max_i = n-1

    print(a_s[a_max_i])
