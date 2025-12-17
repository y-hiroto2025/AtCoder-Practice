"""
問題URL: https://atcoder.jp/contests/abc426/tasks/abc426_b
----------------------------------------------------
結果
・自力（5min）
----------------------------------------------------
"""

def main():
    S = input()
    if S.count(S[0]) == 1:
        print(S[0])
    else:
        for i in range(1, len(S)):
            if S[i] != S[0]:
                print(S[i])
                break

if __name__ == "__main__":
    main()