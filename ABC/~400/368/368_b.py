"""
問題URL: https://atcoder.jp/contests/abc368/tasks/abc368_b
----------------------------------------------------
結果
・自力（6min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0

    while True:
        A.sort(A, reverse=True)
        
        if A[1] <= 0:
            break

        A[0] -= 1
        A[1] -= 1

        ans += 1

    print(ans)


if __name__ == "__main__":
    main()