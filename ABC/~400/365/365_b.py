"""
問題URL: https://atcoder.jp/contests/abc365/tasks/abc365_b
----------------------------------------------------
結果
・自力（4min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(A.index(sorted(A)[-2]) + 1)


if __name__ == "__main__":
    main()