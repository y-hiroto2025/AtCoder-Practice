"""
問題URL: https://atcoder.jp/contests/abc136/tasks/abc136_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    H = list(map(int, input().split()))

    H[0] -= 1

    for i in range(1, N):
        if H[i-1] <= H[i] - 1:
            H[i] -= 1
    
    if H == sorted(H):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()