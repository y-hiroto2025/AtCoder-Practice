"""
問題URL: https://atcoder.jp/contests/abc093/tasks/abc093_b
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    A, B, K = map(int, input().split())

    for i in range(A, min(A+K, B+1)):
        print(i)

    for i in range(max(B-K+1, A+K), B+1):
        print(i)


if __name__ == "__main__":
    main()