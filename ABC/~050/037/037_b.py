"""
問題URL: https://atcoder.jp/contests/abc037/tasks/abc037_b
----------------------------------------------------
結果
・自力（3min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, Q = map(int, input().split())
    a = [0] * N
    
    for _ in range(Q):
        L_i, R_i, T_i = map(int, input().split())
        for i in range(L_i - 1, R_i):
            a[i] = T_i
        """
        a[L_i - 1: R_i] = [T_i] * (R_i - L_i + 1)
        """
    
    print(*a, sep="\n")

if __name__ == "__main__":
    main()