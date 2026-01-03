"""
問題URL: https://atcoder.jp/contests/abc345/tasks/abc345_b
----------------------------------------------------
結果
・自力（10min）

解法ポイント、学び
・
----------------------------------------------------
"""
def main():
    X = int(input())
    """
    if X % 10 == 0:
        ans = X // 10
    else:
        ans = X // 10 + 1
    """
    ans = (X + 10 - 1) // 10

    print(ans)

if __name__ == "__main__":
    main()