"""
問題URL: https://atcoder.jp/contests/abc379/tasks/abc379_b
----------------------------------------------------
結果
・自力（3min）
----------------------------------------------------
"""
def main():
    S = input().lstrip("|")

    ans = []
    curr = 0
    for i in range(len(S)):
        if S[i] == "-":
            curr += 1
        else:
            ans.append(curr)
            curr = 0

    print(*ans)


if __name__ == "__main__":
    main()