"""
問題URL: https://atcoder.jp/contests/abc472/tasks/abc472_b
----------------------------------------------------
結果
・3min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    L = list(map(int, input().split()))

    ans = sum(L)
    a, b = sum(L), 0

    for i in range(N):
        a -= L[i]
        b += L[i]

        ans = min(ans, abs(a-b))

    print(ans)


if __name__ == "__main__":
    main()