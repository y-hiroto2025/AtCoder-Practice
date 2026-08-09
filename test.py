"""
url: https://atcoder.jp/contests/abc074/tasks/abc074_b
"""

import sys

input = sys.stdin.readline

def main():
    N = int(input())
    K = int(input())
    x = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        ans += min(x[i], K-x[i]) * 2

    print(ans)

if __name__ == "__main__":
    main()