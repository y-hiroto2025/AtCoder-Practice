"""
問題URL: https://atcoder.jp/contests/abc370/tasks/abc370_b
----------------------------------------------------
結果
・自力（13min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    ans = A[0][0]
    for i in range(1, N):
        if ans >= i+1:
            ans = A[ans-1][i]
        else:
            ans = A[i][ans-1]

    print(ans)

if __name__ == "__main__":
    main()