"""
問題URL: https://atcoder.jp/contests/abc140/tasks/abc140_c
----------------------------------------------------
結果
・11min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    B = list(map(int, input().split()))

    ans = B[0]

    if N==2:
        print(B[0]*2)
        return

    for i in range(N-1-1):
        ans += min(B[i], B[i+1])

    ans += B[-1]

    print(ans)


if __name__ == "__main__":
    main()