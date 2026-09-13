"""
問題URL: https://atcoder.jp/contests/abc475/tasks/abc475_b
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))

    one, ten, hun = 0, 0, 0

    for a in A:
        a = (-a) % 1000

        hun += a // 100
        ten += a // 10 % 10
        one += a%10

    print(one,ten,hun)


if __name__ == "__main__":
    main()