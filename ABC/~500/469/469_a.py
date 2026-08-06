"""
問題URL: https://atcoder.jp/contests/abc469/tasks/abc469_a
----------------------------------------------------
結果
・1min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    print(N-K+1)


if __name__ == "__main__":
    main()