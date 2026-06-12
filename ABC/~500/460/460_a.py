"""
問題URL: https://atcoder.jp/contests/abc460/tasks/abc460_a
----------------------------------------------------
結果
・自力(1.5min)
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, M  =map(int, input().split())

    ans = 0
    while M!= 0:
        x = N % M
        M = x
        ans += 1

    print(ans)


if __name__ == "__main__":
    main()