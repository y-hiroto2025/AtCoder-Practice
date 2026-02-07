"""
問題URL: https://atcoder.jp/contests/abc011/tasks/abc011_b
----------------------------------------------------
結果
・自力（3min）
----------------------------------------------------
"""
def main():
    S = input().strip()
    """if len(S) > 1:
        print(S[0].upper() + S[1:].lower())
    else:
        print(S.upper())"""
    print(S.capitalize())

if __name__ == "__main__":
    main()