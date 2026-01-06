"""
問題URL: https://atcoder.jp/contests/abc353/tasks/abc353_b
----------------------------------------------------
結果
・ギブアップ

解法ポイント、学び
・
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 0
    remainder = K
    for i in range(N):
        if remainder < A[i]:
            remainder = K
            ans += 1
        remainder -= A[i]

    print(ans + 1)

if __name__ == "__main__":
    main()