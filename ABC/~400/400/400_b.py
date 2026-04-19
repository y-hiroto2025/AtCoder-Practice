"""
問題URL: https://atcoder.jp/contests/abc400/tasks/abc400_b
----------------------------------------------------
結果
・自力（5min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())

    ans = 1
    for i in range(1, M+1):
        ans += N ** i
    
    if ans > 10 ** 9:
        print("inf")
    else:
        print(ans)


if __name__ == "__main__":
    main()