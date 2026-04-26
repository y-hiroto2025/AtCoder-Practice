"""
問題URL: https://atcoder.jp/contests/abc415/tasks/abc415_b
----------------------------------------------------
結果
・自力（4min）
----------------------------------------------------
"""
def main():
    S = input().strip()

    ans = []

    for i in range(len(S)):
        if S[i] == "#":
            ans.append(i+1)
    
    for j in range(0, len(ans), 2):
        print(f"{ans[j]},{ans[j+1]}")


if __name__ == "__main__":
    main()