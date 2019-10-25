pieces_num, markpoints_num = map(int, input().split())
markpoints = sorted(map(int, input().split()))

distances = []
for markpoints_i in range(1, markpoints_num):
    distances.append(markpoints[markpoints_i] - markpoints[markpoints_i - 1])
distances.sort()

print(sum(distances[:1 - pieces_num] if pieces_num != 1 else distances))
