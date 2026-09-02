"""
url: https://atcoder.jp/contests/agc012/tasks/agc012_a
"""

import sys

input = sys.stdin.readline

def main():
    N = int(input())
    a = sorted(map(int, input().split()), reverse=True)

    ans = 0
    for i in range(N * 2):
        if i % 2 != 0:
            ans += a[i]

    print(ans)
    

if __name__ == "__main__":
    main()