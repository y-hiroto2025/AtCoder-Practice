"""
問題URL: https://atcoder.jp/contests/abc115/tasks/abc115_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    h = sorted([int(input()) for _ in range(N)])

    ans = 10000000000
    for i in range(N-K+1):
        ans = min(ans, h[i+K-1] - h[i])
    
    print(ans)


if __name__ == "__main__":
    main()