"""
問題URL: https://atcoder.jp/contests/abc087/tasks/abc087_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    A = []
    A.append(list(map(int, input().split())))
    A.append(list(map(int, input().split())))

    ans = 0
    top = A[0][0]
    bottom = sum(A[1])

    for i in range(N):
        ans = max(ans, top + bottom)

        if i+1 < N:
            top += A[0][i+1]
            bottom -= A[1][i]

    print(ans)


if __name__ == "__main__":
    main()