"""
問題URL: https://atcoder.jp/contests/abc461/tasks/abc461_b
----------------------------------------------------
結果
・自力（3min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    for i in range(N):
        if i != B[A[i]-1] - 1:
            print("No")
            return
    
    print("Yes")


if __name__ == "__main__":
    main()