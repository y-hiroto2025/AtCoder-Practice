"""
問題URL: https://atcoder.jp/contests/abc098/tasks/abc098_b
----------------------------------------------------
結果
・自力（5min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    S = input().strip()

    ans = 0

    for i in range(1, N-1):
        X = set(S[:i])
        Y = set(S[i:])

        ans = max(ans, len(X - (X - Y)))
    
    print(ans)

if __name__ == "__main__":
    main()