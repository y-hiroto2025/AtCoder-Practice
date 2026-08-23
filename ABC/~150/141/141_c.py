"""
問題URL: https://atcoder.jp/contests/abc141/tasks/abc141_c
----------------------------------------------------
結果
・4min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, K, Q = map(int, input().split())

    std = 0
    points = [K]*N

    for _ in range(Q):
        a = int(input())

        points[a-1] += 1
        std += 1

    for i in range(N):
        if points[i] <= std:
            print("No")
        else:
            print("Yes")


if __name__ == "__main__":
    main()