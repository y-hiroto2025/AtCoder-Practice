"""
問題URL: https://atcoder.jp/contests/abc399/tasks/abc399_b
----------------------------------------------------
結果
・自力（11min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    P = list(map(int, input().split()))
    P_sorted = sorted(set(P), reverse=True)
    r = 1

    ans = [0] * N
    for point in P_sorted:
        x = point
        k = len([p for p in P if p == x])

        for i in range(N):
            if P[i] == x:
                ans[i] = r
        
        r += k
    print(*ans, sep="\n")

if __name__ == "__main__":
    main()