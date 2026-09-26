"""
問題URL: https://atcoder.jp/contests/abc046/tasks/abc046_
----------------------------------------------------
結果
・3min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, K = map(int, input().split())

    ans = K
    for _ in range(N-1):
        ans *= K-1

    print(ans)


if __name__ == "__main__":
    main()