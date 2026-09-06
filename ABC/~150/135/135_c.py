"""
問題URL: https://atcoder.jp/contests/abc135/tasks/abc135_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = 0

    for i in range(N):
        num1 = min(A[i], B[i])
        ans += num1

        A[i] -= num1
        B[i] -= num1

        if B[i] > 0:
            num2 = min(A[i+1], B[i])
            ans += num2

            A[i+1] -= num2
            B[i] -= num2

    print(ans)


if __name__ == "__main__":
    main()