"""
問題URL: https://atcoder.jp/contests/abc151/tasks/abc151_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())

    is_ac = [False] * (N+1)
    wa_cnt = [0] * (N+1)

    ac_total = 0
    wa_total = 0

    for _ in range(M):
        p, s = input().split()
        p = int(p)

        if is_ac[p]:
            continue

        if s == "AC":
            is_ac[p] = True
            ac_total += 1
            wa_total += wa_cnt[p]
        else:
            wa_cnt[p] += 1

    print(ac_total, wa_total)


if __name__ == "__main__":
    main()