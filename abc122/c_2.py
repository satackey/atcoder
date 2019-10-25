import bisect

n, q = map(int, input().split())
s = input()

ac_positions = []
for i in range(n):
    if s[i:i + 2] == 'AC':
        ac_positions.append(i + 1)

questions = []
for i in range(q):
    question = list(map(int, input().split()))
    ac_count = 0

    explore_ac_positions = ac_positions[
                           bisect.bisect_left(ac_positions, question[0]):
                           bisect.bisect_right(ac_positions, question[1] - 1)]

    ac_count = len(explore_ac_positions)

    print(ac_count)
