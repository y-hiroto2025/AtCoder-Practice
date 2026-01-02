"""
問題URL: https://atcoder.jp/contests/abc343/tasks/abc343_b
----------------------------------------------------
結果
・自力（7min）

解法ポイント、学び
・
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    
    for i in range(N):
        ans = []
        for j in range(N):
            if A[i][j] == 1:
                ans.append(j + 1)
        print(*ans)

if __name__ == "__main__":
    main()