"""
問題URL: https://atcoder.jp/contests/abc468/tasks/abc468_a
----------------------------------------------------
結果
・1min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0

    for i in range(N-2):
        if (A[i] < A[i+1]) and (A[i+1] > A[i+2]):
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()