trees_num, illuminations_num = map(int, input().split())
trees = sorted(int(input()) for _ in range(trees_num))

diffs = []

for i in range(trees_num - illuminations_num + 1):
    diffs.append(trees[i+illuminations_num-1] - trees[i])

print(min(diffs))
