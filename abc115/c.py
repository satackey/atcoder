trees_num, illuminations_num = map(int, input().split())
trees = sorted(int(input()) for _ in range(trees_num))

differences = sorted(trees[i] - trees[i-1] for i in range(1, trees_num))
print(sum(differences[:illuminations_num - 1]))
