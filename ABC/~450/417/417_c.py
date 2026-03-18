"""
問題URL: https://atcoder.jp/contests/abc417/tasks/abc417_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))

    a_i = {}
    ans = 0

    for j in range(N):
        cood_j = j - A[j]
        cood_i = j + A[j]

        if cood_j in a_i:
            ans += a_i[cood_j]
        
        if cood_i in a_i:
            a_i[cood_i] += 1
        else:
            a_i[cood_i] = 1

    print(ans)


if __name__ == "__main__":
    main()