"""
問題URL: https://atcoder.jp/contests/abc320/tasks/abc320_b
----------------------------------------------------
結果
・自力（17min）
----------------------------------------------------
"""
def main():
    S = input()
    ans = 1

    for i in range(0, len(S)):
        for j in range(i + 1, len(S) + 1):
            s = S[i:j]

            if s == s[::-1]:
                ans = max(len(s), ans)

    print(ans)


if __name__ == "__main__":
    main()