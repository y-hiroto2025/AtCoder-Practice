"""
問題URL: https://atcoder.jp/contests/abc055/tasks/abc055_b
----------------------------------------------------
結果
・2min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())

    ans = 1

    for i in range(2, N+1):
        ans *= i
        ans %= 1e9 + 7

    print(int(ans))


if __name__ == "__main__":
    main()