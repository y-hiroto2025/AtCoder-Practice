"""
問題URL: https://atcoder.jp/contests/abc122/tasks/abc122_b
----------------------------------------------------
結果
・5min
----------------------------------------------------
"""
def main():
    S = input().strip()
    s_set = {"A", "C", "G", "T"}

    ans = 0
    curr = 0
    flg = False

    for i in range(len(S)):
        if S[i] in s_set:

            if flg:
                curr += 1
            else:
                flg = True
                curr = 1

            ans = max(ans, curr)

        else:
            flg = False

    print(ans)


if __name__ == "__main__":
    main()