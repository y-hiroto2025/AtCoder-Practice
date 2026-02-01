"""
問題URL: https://atcoder.jp/contests/abc050/tasks/abc050_b
----------------------------------------------------
結果
・自力（7min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    T = list(map(int, input().split()))
    M = int(input())
    for _ in range(M):
        tmp = T[:]
        P_i, X_i = map(int, input().split())
        tmp[P_i - 1] = X_i
        print(sum(tmp))

if __name__ == "__main__":
    main()