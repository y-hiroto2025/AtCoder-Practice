"""
問題URL: https://atcoder.jp/contests/abc373/tasks/abc373_b
----------------------------------------------------
結果
・
----------------------------------------------------
"""
def main():
    S = input().strip()
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    ans = 0
    idx = S.index("A")
    for i in range(1, 26):
        dist = abs(idx - S.index(alph[i]))
        idx = S.index(alph[i])
        ans += dist

    print(ans)

if __name__ == "__main__":
    main()