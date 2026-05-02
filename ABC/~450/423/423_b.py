"""
問題URL: https://atcoder.jp/contests/abc423/tasks/abc423_b
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    L = list(map(int, input().split()))

    right_one = 0
    left_one = 0

    for i in range(N):
        if L[i] == 1:
            right_one = i
            break
    
    for i in range(N):
        if L[N-i-1] == 1:
            left_one = N-i-1
            break
    
    print(left_one - right_one)


if __name__ == "__main__":
    main()