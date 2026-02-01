"""
問題URL: https://atcoder.jp/contests/abc328/tasks/abc328_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, Q = map(int, input().split())
    S = input().strip()
    prefix = [0] * N

    for i in range(1, N):
        if S[i] == S[i - 1]:
            prefix[i] = prefix[i - 1] + 1
        else:
            prefix[i] = prefix[i - 1]
    
    for _ in range(Q):
        l_i, r_i = map(int, input().split())
        print(prefix[r_i - 1] - prefix[l_i - 1])


if __name__ == "__main__":
    main()