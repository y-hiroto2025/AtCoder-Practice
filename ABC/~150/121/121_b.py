"""
問題URL: https://atcoder.jp/contests/abc121/tasks/abc121_b
----------------------------------------------------
結果
・自力（6min）
----------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    ans = 0

    for _ in range(N):
        A_i = list(map(int, input().split()))

        """if sum(A_i[j] * B[j] for j in range(M)) + C > 0:
            ans += 1"""
        
        total = sum(a * b for a, b in zip(A_i, B))
        if total + C > 0:
            ans += 1

    print(ans)

if __name__ == "__main__":
    main()