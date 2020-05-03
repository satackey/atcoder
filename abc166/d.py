import sys

def debug(*args):
    print(*args, file=sys.stderr)


x_diff_of_5th_factor = int(input())


for a in range(-118, 119):
    for b in range(-119, 118):
        if a ** 5 - b ** 5 == x_diff_of_5th_factor:
            print('{} {}'.format(a, b))
            sys.exit(0)

sys.exit(1)
