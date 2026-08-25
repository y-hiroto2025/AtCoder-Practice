"""
問題URL: https://atcoder.jp/contests/abc059/tasks/abc059_b
----------------------------------------------------
結果
・1min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    A = int(input())
    B = int(input())

    if A>B:
        print("GREATER")
    elif A<B:
        print("LESS")
    else:
        print("EQUAL")


if __name__ == "__main__":
    main()