"""
問題URL: https://atcoder.jp/contests/abc132/tasks/abc132_c
----------------------------------------------------
結果
・4min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    d = sorted(map(int, input().split()))

    ans = d[N//2] - d[N//2-1]

    print(ans)


if __name__ == "__main__":
    main()