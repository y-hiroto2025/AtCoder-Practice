"""
問題URL: https://atcoder.jp/contests/abc394/tasks/abc394_b
----------------------------------------------------
結果
・自力（4min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())

    S = []

    for _ in range(N):
        S.append(input().strip())
    
    S.sort(key=lambda s: len(s))
    
    print("".join(S))


if __name__ == "__main__":
    main()