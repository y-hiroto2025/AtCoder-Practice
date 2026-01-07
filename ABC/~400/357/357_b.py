"""
問題URL: https://atcoder.jp/contests/abc357/tasks/abc357_b
----------------------------------------------------
結果
・自力（4min）
----------------------------------------------------
"""
def main():
    S = input()
    """up_count = sum([1 for i in range(S_len) if S[i].isupper()])"""
    # Trueは1, Falseは0として扱われる。
    up_count = sum([c.isupper for c in S])
    if up_count > len(S) / 2:
        print(S.upper())
    else:
        print(S.lower())

if __name__ == "__main__":
    main()