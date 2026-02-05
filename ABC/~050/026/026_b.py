"""
問題URL: https://atcoder.jp/contests/abc026/tasks/abc026_b
----------------------------------------------------
結果
・自力（6min）
----------------------------------------------------
"""
import sys
from math import pi

input = sys.stdin.readline

def main():
    N = int(input())
    ans = 0
    R = [int(input()) for _ in range(N)]
    R.sort()

    for i in range(N):
        R_i = R[i]
        if i % 2 == 1:
            ans += R_i ** 2
        else:
            ans -= R_i ** 2
    ans *= pi
    print(abs(ans))

if __name__ == "__main__":
    main()