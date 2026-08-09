"""
問題URL: https://atcoder.jp/contests/abc470/tasks/abc470_b
----------------------------------------------------
結果
・5min
----------------------------------------------------
"""
import sys
from collections import Counter

input = sys.stdin.readline

def main():
    N = int(input())
    C = list(map(int, input().split()))

    C_max = max(Counter(C).values())
    print(N-C_max)


if __name__ == "__main__":
    main()