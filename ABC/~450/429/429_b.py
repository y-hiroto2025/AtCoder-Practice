"""
問題URL: https://atcoder.jp/contests/abc429/tasks/abc429_b
----------------------------------------------------
結果
・自力（1min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    sum_A = sum(A)
    for i in range(N):
        if sum_A - A[i] == M:
            print("Yes")
            return
    
    print("No")


if __name__ == "__main__":
    main()