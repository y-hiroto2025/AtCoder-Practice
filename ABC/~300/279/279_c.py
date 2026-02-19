"""
問題URL: https://atcoder.jp/contests/abc279/tasks/abc279_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    H, W = map(int, input().split())
    S = sorted(zip(*[input().strip() for _ in range(H)]))
    T = sorted(zip(*[input().strip() for _ in range(H)]))

    if S == T:
        print("Yes")

    else:
        print("No")


if __name__ == "__main__":
    main()