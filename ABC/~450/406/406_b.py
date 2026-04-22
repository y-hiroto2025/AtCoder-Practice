"""
問題URL: https://atcoder.jp/contests/abc406/tasks/abc406_b
----------------------------------------------------
結果
・自力（3min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ans = A[0]

    for i in range(1, N):

        if len(str(ans * A[i])) > K:
            ans = 1
        else:
            ans *= A[i]
        
    print(ans)


if __name__ == "__main__":
    main()