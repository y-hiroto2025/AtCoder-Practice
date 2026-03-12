import sys
from itertools import product
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    R = map(int, input().split())

    ranges = [range(1, r + 1) for r in R]

    for conb in product(*ranges):

        if sum(conb) % K == 0:
            print(*conb)


if __name__ == "__main__":
    main()