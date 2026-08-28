"""
問題URL: https://atcoder.jp/contests/abc042/tasks/abc042_b
----------------------------------------------------
結果
・1min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, L = map(int, input().split())

    S_list = []

    for _ in range(N):
        S_list.append(input().strip())

    print(*sorted(S_list), sep="")


if __name__ == "__main__":
    main()