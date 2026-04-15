"""
問題URL: https://atcoder.jp/contests/abc393/tasks/abc393_b
----------------------------------------------------
結果
・自力（10min）
----------------------------------------------------
"""
from itertools import combinations
def main():
    S = input().strip()

    ans = 0
    comb = list(combinations(range(len(S)), 3))
    
    for c in comb:
        if c[1]-c[0] == c[2]-c[1]:
            if S[c[0]]=="A" and S[c[1]]=="B" and S[c[2]]=="C":
                ans += 1
    
    print(ans)


if __name__ == "__main__":
    main()