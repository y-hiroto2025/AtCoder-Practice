"""
問題URL: https://atcoder.jp/contests/abc359/tasks/abc359_b
----------------------------------------------------
結果
・自力（5min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0

    for i in range(N * 2 - 2):
        if A[i] == A[i + 2]:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()