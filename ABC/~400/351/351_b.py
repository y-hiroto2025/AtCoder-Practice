"""
問題URL: https://atcoder.jp/contests/abc351/tasks/abc351_b
----------------------------------------------------
結果
・自力（4min）

解法ポイント、学び
・
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    A = [input().strip() for _ in range(N)]
    B = [input().strip() for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if A[i][j] != B[i][j]:
                print(i + 1, j + 1)
                return

if __name__ == "__main__":
    main()