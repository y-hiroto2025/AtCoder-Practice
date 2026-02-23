"""
問題URL: https://atcoder.jp/contests/abc326/tasks/abc326_c
----------------------------------------------------
----------------------------------------------------
"""
import sys
import bisect
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    A = sorted(map(int, input().split()))

    ans = 0
    for i in range(N):
        r = bisect.bisect_left(A, A[i]+M)
        ans = max(ans, r-i)

    print(ans)


if __name__ == "__main__":
    main()