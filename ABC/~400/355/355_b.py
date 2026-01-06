"""
問題URL: https://atcoder.jp/contests/abc355/tasks/abc355_b
----------------------------------------------------
結果
・自力（5min）

解法ポイント、学び
・
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = sorted(A + B)

    A_set = set(A)

    for i in range(N + M - 1):
        if C[i] in A_set and C[i + 1] in A_set:
            print("Yes")
            return
        
    print("No")

if __name__ == "__main__":
    main()