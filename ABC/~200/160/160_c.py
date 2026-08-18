"""
問題URL: https://atcoder.jp/contests/abc160/tasks/abc160_c
----------------------------------------------------
結果
・12min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))

    max_diff = 0
    ans = 0

    for i in range(1, N+1):
        if i != N:
            diff = A[i] - A[i-1]
        else:
            diff = K - A[i-1] + A[0]

        ans += diff

        if max_diff < diff:
            max_diff = diff

    print(ans - max_diff)


if __name__ == "__main__":
    main()