import bisect

n, q = map(int, input().split())
s = input()

questions = []
for i in range(q):
    questions.append(list(map(int, input().split())))

ac_positions = []
for i in range(n):
    if s[i:i + 2] == 'AC':
        ac_positions.append(i + 1)

for question in questions:
    ac_count = 0

    explore_ac_positions = ac_positions[
                           bisect.bisect_left(ac_positions, question[0]):
                           bisect.bisect_right(ac_positions, question[1])]
    for ac_position in explore_ac_positions:
        if question[0] <= ac_position and ac_position + 1 <= question[1]:
            ac_count += 1

    print(ac_count)
