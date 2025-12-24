"""
問題URL: https://atcoder.jp/contests/abc317/tasks/abc317_b
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
    A = set(map(int, input().split()))
    B = set(x for x in range(min(A), max(A) + 1))

    print(*(B - A))

if __name__ == "__main__":
    main()