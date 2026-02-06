"""
問題URL: https://atcoder.jp/contests/abc410/tasks/abc410_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, Q = map(int, input().split())
    A = [i for i in range(1, N + 1)]

    offset = 0

    for _ in range(Q):
        query = list(map(int, input().split()))

        if query[0] == 1:
            x, y = query[1], query[2]
            real_index = (x - 1 + offset) % N
            A[real_index] = y
        elif query[0] == 2:
            x = query[1]
            real_index = (x - 1 + offset) % N
            print(A[real_index])
        else:
            k = query[1]
            offset = (offset + k) % N


if __name__ == "__main__":
    main()