"""
問題URL: https://atcoder.jp/contests/abc467/tasks/abc467_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, M  = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    cost0 = 0
    curr0 = 0
    if A[0] != curr0:
        cost0 = 1

    cost1 = 0
    curr1 = 1
    if A[0] != curr1:
        cost1 += 1

    for i in range(N-1):
        curr0 ^= B[i]
        if A[i+1] != curr0:
            cost0 += 1

        curr1 ^= B[i]
        if A[i+1] != curr1:
            cost1 += 1

    print(min(cost0, cost1))

if __name__ == "__main__":
    main()