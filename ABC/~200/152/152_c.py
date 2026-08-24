"""
問題URL: https://atcoder.jp/contests/abc152/tasks/abc152_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    P = list(map(int, input().split()))

    ans = 0
    min_num = float('inf')

    for p in P:
        if p <= min_num:
            ans += 1
            min_num = p

    print(ans)


if __name__ == "__main__":
    main()