"""
問題URL: https://atcoder.jp/contests/abc224/tasks/abc224_c
----------------------------------------------------
結果
・自力（11min）
----------------------------------------------------
"""
import sys
from itertools import combinations

input = sys.stdin.readline

def main():
    N = int(input())
    coods = []

    for _ in range(N):
        x, y = map(int, input().split())
        coods.append((x, y))
    
    comb = list(combinations(coods, 3))

    ans = 0

    for c in comb:
        c_1 = c[0]
        c_2 = c[1]
        c_3 = c[2]

        if (c_3[0]-c_2[0]) * (c_2[1]-c_1[1]) != (c_2[0]-c_1[0]) * (c_3[1]-c_2[1]):
            ans += 1
    
    print(ans)


if __name__ == "__main__":
    main()