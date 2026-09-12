"""
問題URL: https://atcoder.jp/contests/abc474/tasks/abc474_c
----------------------------------------------------
結果
・17min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, Q = map(int, input().split())
    P = list(map(int, input().split()))

    idx_list = [0] * N
    for i, val in enumerate(P):
        idx_list[val-1] = i

    for q in range(Q):
        a = int(input())

        idx_list[a-1] = N + q+1

    idx_list = sorted([(idx, num+1) for num, idx in enumerate(idx_list)])

    ans_list = [0] * N
    curr_idx = 0

    for ip in idx_list:
        ans_list[curr_idx] = ip[1]

        curr_idx += 1

    print(*ans_list)        


if __name__ == "__main__":
    main()