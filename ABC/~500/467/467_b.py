"""
問題URL: https://atcoder.jp/contests/abc467/tasks/abc467_b
----------------------------------------------------
結果
・3min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())

    X, Y = 10000, 10000

    for _ in range(N):
        a, b, s = input().split()
        a = int(a)
        b = int(b)

        if s == "keep":
            X -= b
            Y -= a
        else:
            X -= a
            Y -= a

    print(Y - X)


if __name__ == "__main__":
    main()