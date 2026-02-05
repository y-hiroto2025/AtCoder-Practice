"""
問題URL: https://atcoder.jp/contests/abc028/tasks/abc028_b
----------------------------------------------------
結果
・自力（3min）
----------------------------------------------------
"""
def main():
    S = input().strip()
    moji_dict = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}

    for s in S:
        moji_dict[s] += 1
    ans = moji_dict.values()
    print(*ans)

if __name__ == "__main__":
    main()