"""
問題URL: https://atcoder.jp/contests/abc457/tasks/abc457_c
----------------------------------------------------
結果
・自力（12min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, K = map(int, input().split())

    LA = []
    for _ in range(N):
        LA.append(list(map(int, input().split())))

    C = list(map(int, input().split()))

    B_len = []
    for i in range(N):
        L = LA[i][0]

        B_len.append((L, C[i]))

        if K - L * C[i] > 0:
            K -= L * C[i]
        else:
            print(LA[i][(K-1) % L + 1])
            break


if __name__ == "__main__":
    main()