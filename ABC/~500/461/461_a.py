"""
問題URL: https://atcoder.jp/contests/abc461/tasks/abc461_a
----------------------------------------------------
結果
・自力（1min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    A, D = map(int, input().split())
    if A <= D:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()