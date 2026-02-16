"""
問題URL: https://atcoder.jp/contests/abc189/tasks/abc189_b
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, X = map(int, input().split())

    alcohol = 0
    ans = -1
    for i in range(N):
        V, P = map(int, input().split())
        alcohol += V * P
        if alcohol > X * 100:
            ans = i + 1
            break

    print(ans)


if __name__ == "__main__":
    main()