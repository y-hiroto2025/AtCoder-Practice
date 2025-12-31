"""
問題URL: https://atcoder.jp/contests/abc334/tasks/abc334_b
----------------------------------------------------
結果
・ギブアップ

解法ポイント、学び
・
----------------------------------------------------
"""
def main():
    A, M, L, R = map(int, input().split())
    L -= A
    R -= A

    print(R // M - (L - 1) // M)

if __name__ == "__main__":
    main()