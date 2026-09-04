"""
問題URL: https://atcoder.jp/contests/abc144/tasks/abc144_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())

    ans = float('inf')

    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            j = N // i

            ans = min(ans, i+j-2)

    print(ans)


if __name__ == "__main__":
    main()