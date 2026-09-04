"""
url: https://atcoder.jp/contests/agc019/tasks/agc019_a
"""

import sys

input = sys.stdin.readline

def main():
    Q, H, S, D = map(int, input().split())
    N = int(input())

    H = min(H, Q * 2)
    S = min(S, H * 2)

    if S*2 <=  D:
        ans = S * N
    else:

        ans = D * (N // 2) + (N % 2) * S

    print(ans)
    

if __name__ == "__main__":
    main()