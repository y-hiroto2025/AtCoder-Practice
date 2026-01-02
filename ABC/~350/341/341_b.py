"""
問題URL: https://atcoder.jp/contests/abc341/tasks/abc341_b
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    for i in range(N - 1):
        S_i, T_i = map(int, input().split())
        A[i + 1] += T_i * (A[i] // S_i)

    print(A[N - 1])

if __name__ == "__main__":
    main()