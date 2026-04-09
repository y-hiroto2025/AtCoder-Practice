"""
問題URL: https://atcoder.jp/contests/abc390/tasks/abc390_b
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))

    for i in range(N-2):
        if A[i]*A[i+2] != A[i+1]*A[i+1]:
            print("No")
            return
    
    print("Yes")


if __name__ == "__main__":
    main()