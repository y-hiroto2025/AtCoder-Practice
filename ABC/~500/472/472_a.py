"""
問題URL: https://atcoder.jp/contests/abc472/tasks/abc472_a
----------------------------------------------------
結果
・1min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    S = input().strip()

    for s in S:
        if s != "A":
            print(".", end="")
        else:
            print(s, end="")


if __name__ == "__main__":
    main()