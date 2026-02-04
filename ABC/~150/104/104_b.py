"""
問題URL: https://atcoder.jp/contests/abc104/tasks/abc104_b
----------------------------------------------------
結果
・自力（7min）
----------------------------------------------------
"""
import collections

def main():
    S = input().strip()
    cond1 = S[0] == "A"
    cond2 = collections.Counter(S[2: -1])["C"] == 1
    cond3 = sum(map(str.isupper, S)) == 2

    if cond1 and cond2 and cond3:
        print("AC")
    else:
        print("WA")


if __name__ == "__main__":
    main()