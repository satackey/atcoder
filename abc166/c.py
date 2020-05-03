from sys import stderr

def debug(*args):
    print(*args, file=stderr)

n_observatory_num, m_roads_num = map(int, input().split())
hi_heights = list(map(int, input().split()))

# def get_height_for(a_observaotry):
#     return hi_heights[a_observaotry+1]

ab_roads_fromto = [map(int, input().split()) for _ in range(m_roads_num)]


observatory_x_connected_to = {}

for a, b in ab_roads_fromto:
    a -= 1
    b -= 1
    if not a in observatory_x_connected_to:
        observatory_x_connected_to[a] = []
    if not b in observatory_x_connected_to:
        observatory_x_connected_to[b] = []

    observatory_x_connected_to[a].append(b)
    observatory_x_connected_to[b].append(a)

# debug(observatory_x_connected_to)

result = 0
for observatory_i, observatory_i_height in enumerate(hi_heights):
    # observatory_i_height = get_height_for(observatory_i)
    if not observatory_i in observatory_x_connected_to:
        # debug('good no connection' + str(observatory_i))
        result += 1
        continue

    good = True
    for connected_to in observatory_x_connected_to[observatory_i]:
        if observatory_i_height <= hi_heights[connected_to]:
            good = False
            # debug('not good' + str(observatory_i))
            break
    
    if good:
        # debug('good highest' + str(observatory_i))
        result += 1

print(result)
