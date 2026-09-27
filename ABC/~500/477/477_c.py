"""
問題URL: https://atcoder.jp/contests/abc477/tasks/abc477_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    Q = int(input())
    S = input().strip()
    T = input().strip()

    len_S = len(S)
    len_T = len(T)

    is_match = [0] * len_S
    for i in range(len_S - len_T + 1):
        if S[i : i + len_T] == T:
            is_match[i] = 1

    pfx_sum = [0] * (len_S + 1)
    for i in range(len_S):
        pfx_sum[i + 1] += pfx_sum[i] + is_match[i]

    ans = []

    for _ in range(Q):
        L, R = map(int, input().split())

        if R-L+1 < len_T:
            ans.append("No")
            continue

        start = L - 1
        end = R - len_T

        cnt = pfx_sum[end + 1] - pfx_sum[start]
        if cnt > 0:
            ans.append("Yes")
        else:
            ans.append("No")

    print(*ans, sep="\n")

        
if __name__ == "__main__":
    main()