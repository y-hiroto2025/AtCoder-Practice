"""
問題URL: https://atcoder.jp/contests/abc363/tasks/abc363_b
----------------------------------------------------
結果
・自力（5min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, T, P = map(int, input().split())
    L = sorted(map(int, input().split()))

    print(max(T - L[-P], 0))

if __name__ == "__main__":
    main()