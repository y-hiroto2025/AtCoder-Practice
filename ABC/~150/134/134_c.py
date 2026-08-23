"""
問題URL: https://atcoder.jp/contests/abc134/tasks/abc134_c
----------------------------------------------------
結果
・5min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    A = []
    for _ in range(N):
        A.append(int(input()))

    A_sorted = sorted(A, reverse=True)

    for i in range(N):
        if A[i] != A_sorted[0]:
            print(A_sorted[0])
        else:
            print(A_sorted[1])
        

if __name__ == "__main__":
    main()