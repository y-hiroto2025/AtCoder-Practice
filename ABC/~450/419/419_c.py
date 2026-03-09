"""
問題URL: https://atcoder.jp/contests/abc419/tasks/abc419_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())

    left = 1000000000
    right = 1
    upper = 1
    down = 1000000000
    for _ in range(N):
        R, C = map(int, input().split())
        left = min(left, R)
        right = max(right, R)
        upper = max(upper, C)
        down = min(down, C)
    
    print(max((right-left+1) // 2, (upper-down+1) // 2))


if __name__ == "__main__":
    main()