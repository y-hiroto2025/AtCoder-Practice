"""
問題URL: https://atcoder.jp/contests/abc475/tasks/abc475_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, S, L = map(int, input().split())
    A = list(map(int, input().split()))

    coords = [0] * (N)
    for i in range(N-1):
        coords[i+1] = coords[i] + A[i]

    ans = 1

    for l in range(S):

        for r in range(S-1, N):
            dist_left = coords[S-1] - coords[l]
            dist_right = coords[r] - coords[S-1]

            min_cost = min(2 * dist_left + dist_right, dist_left + 2 * dist_right)

            if min_cost <= L:
                ans = max(ans, r - l + 1)
            else:
                break

    print(ans)


if __name__ == "__main__":
    main()