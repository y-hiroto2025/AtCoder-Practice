"""
問題URL: https://atcoder.jp/contests/abc459/tasks/abc459_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, Q = map(int, input().split())

    mass = [0] * N
    cnt = [0] * (Q + 2)

    basis = 0

    for _ in range(Q):
        k, x = map(int, input().split())

        if k == 1:
            x -= 1
            mass[x] += 1
            cnt[mass[x]] += 1

            if cnt[basis  +1] == N:
                basis += 1
        
        else:

            if x + basis < len(cnt):
                print(cnt[x + basis])
            else:
                print(0)



if __name__ == "__main__":
    main()