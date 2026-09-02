"""
問題URL: https://atcoder.jp/contests/abc100/tasks/abc100_b
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    D, N = map(int, input().split())

    if N == 100:
        N = 101

    ans = N * (100 ** D)
    print(ans)


if __name__ == "__main__":
    main()