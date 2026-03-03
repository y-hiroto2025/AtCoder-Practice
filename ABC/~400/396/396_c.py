"""
問題URL: https://atcoder.jp/contests/abc396/tasks/abc396_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    B = sorted(map(int, input().split()), reverse=True) #黒の価値
    W = sorted(map(int, input().split()), reverse=True) #白の価値

    ans = 0
    current = 0
    for i in range(N):

        current += B[i]

        if i < M and W[i] > 0:
            current += W[i]

        ans = max(ans, current)

    print(ans)


if __name__ == "__main__":
    main()