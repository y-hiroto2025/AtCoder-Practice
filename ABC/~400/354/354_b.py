"""
問題URL: https://atcoder.jp/contests/abc354/tasks/abc354_b
----------------------------------------------------
結果
・自力（3min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    S = []
    T = 0
    for _ in range(N):
        S_i, C_i = input().split()
        S.append(S_i)
        T += int(C_i)
    S.sort()
    print(S[T % N])

if __name__ == "__main__":
    main()