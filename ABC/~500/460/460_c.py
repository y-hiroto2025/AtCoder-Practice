"""
問題URL: https://atcoder.jp/contests/abc460/tasks/abc460_c
----------------------------------------------------
結果
・自力(12min)
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    A = sorted(map(int, input().split()), reverse=True)
    B = sorted(map(int, input().split()), reverse=True)

    A_idx = 0
    B_idx = 0
    ans = 0

    while A_idx < N and B_idx < M:
        if B[B_idx] <= 2 * A[A_idx]:
            ans += 1
            A_idx += 1
        
        B_idx += 1
    
    print(ans)

if __name__ == "__main__":
    main()