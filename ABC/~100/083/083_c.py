"""
問題URL: https://atcoder.jp/contests/abc083/tasks/abc083_c
----------------------------------------------------
結果
・3min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    X, Y = map(int, input().split())

    ans = 0
    num = X
    while num <= Y:
        num *= 2
        ans += 1

    print(ans)


if __name__ == "__main__":
    main()