antennas = [int(input()) for _ in range(5)]
k = int(input())

# ok = True
#
# for i in range(5):
#     for j in range(i+1, 5):
#         if antennas[j] - antennas[i] > k:
#             ok = False

print("Yay!" if antennas[4] - antennas[0] <= k else ":(")
