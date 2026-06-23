"""
問題URL: https://atcoder.jp/contests/abc463/tasks/abc463_a
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    X, Y = map(int, input().split())

    if (X%16==0) and (Y%9==0):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()