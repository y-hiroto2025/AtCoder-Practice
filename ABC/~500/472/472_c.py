"""
問題URL: https://atcoder.jp/contests/abc472/tasks/abc472_c
----------------------------------------------------
結果
・7min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))

    cal = 0

    for i in range(N):
        if i >= M:
            cal -= A[i-M]

        if cal + A[i] <= K:
            cal += A[i]
            print("Yes")
        else:
            A[i] = 0
            print("No")


if __name__ == "__main__":
    main()