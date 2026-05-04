"""
問題URL: https://atcoder.jp/contests/abc433/tasks/abc433_b
----------------------------------------------------
結果
・自力（3min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))

    for i in range(N):
        A_i = A[i]
        ans = -1

        for j in range(i+1):
            if A_i < A[i-j]:
                ans = i-j + 1
                break
        
        print(ans)


if __name__ == "__main__":
    main()