"""
問題URL: https://atcoder.jp/contests/abc031/tasks/abc031_b
----------------------------------------------------
結果
・自力（3min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    L, H = map(int, input().split())
    N = int(input())
    for i in range(N):
        A_i = int(input())
        if A_i > H:
            print(-1)
        elif A_i < L:
            print(L - A_i)
        else:
            print(0)


if __name__ == "__main__":
    main()