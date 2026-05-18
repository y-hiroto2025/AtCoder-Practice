"""
問題URL: https://atcoder.jp/contests/abc457/tasks/abc457_b
----------------------------------------------------
結果
・自力（4min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())

    la = []
    for _ in range(N):
        la.append(list(map(int, input().split())))

    X, Y = map(int, input().split())

    print(la[X-1][Y])


if __name__ == "__main__":
    main()