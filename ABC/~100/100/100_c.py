"""
問題URL: https://atcoder.jp/contests/abc100/tasks/abc100_c
----------------------------------------------------
結果
・6min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    a = sorted(map(int, input().split()))

    ans = 0

    for i in range(N):

        while a[i] % 2 == 0:
            a[i] //= 2
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()