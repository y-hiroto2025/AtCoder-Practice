"""
問題URL: https://atcoder.jp/contests/abc091/tasks/abc091_b
----------------------------------------------------
結果
・5min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    S = {}

    for _ in range(N):
        s = input().strip()
        if s in S:
            S[s] += 1
        else:
            S[s] = 1

    M = int(input())
    T = {}

    for _ in range(M):
        t = input().strip()
        if t in T:
            T[t] += 1
        else:
            T[t] = 1

    ans = 0
    for key, val in S.items():
        curr = val

        if key in T:
            curr -= T[key]

        ans = max(ans, curr)

    print(ans)



if __name__ == "__main__":
    main()