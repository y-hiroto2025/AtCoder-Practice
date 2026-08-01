"""
問題URL: https://atcoder.jp/contests/abc465/tasks/abc465_c
----------------------------------------------------
結果
・
----------------------------------------------------
"""
import sys
from collections import deque

input = sys.stdin.readline

def main():
    N = int(input())
    S = input().strip()

    a, b = [], []
    rev = False

    for i in range(N):
        if rev:
            a.append(i+1)
        else:
            b.append(i+1)

        if S[i] == 'o':
            rev ^= True

    ans = a[::-1] + b
    if rev:
        ans = ans[::-1]

    print(*ans)

if __name__ == "__main__":
    main()