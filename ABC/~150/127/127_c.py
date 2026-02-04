"""
問題URL: https://atcoder.jp/contests/abc127/tasks/abc127_c
----------------------------------------------------
結果
・自力（10min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    max_L = 1
    min_R = N

    for _ in range(M):
        L_i, R_i = map(int, input().split())
        max_L = max(max_L, L_i)
        min_R = min(min_R, R_i)

    ans = max(0, min_R - max_L + 1)

    print(ans)

if __name__ == "__main__":
    main()