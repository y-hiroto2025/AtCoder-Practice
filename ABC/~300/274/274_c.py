"""
問題URL: https://atcoder.jp/contests/abc274/tasks/abc274_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ameba = [0] * (2*N+1 + 1)
    for i in range(N):
        a = A[i]
        ameba[(i+1)*2] = ameba[a] + 1
        ameba[(i+1)*2 + 1] = ameba[a] + 1

    for k in range(1, 2*N+1 + 1):
        print(ameba[k])


if __name__ == "__main__":
    main()