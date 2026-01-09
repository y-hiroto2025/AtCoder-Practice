"""
問題URL: https://atcoder.jp/contests/abc360/tasks/abc360_b
----------------------------------------------------
結果
・自力（10min）
----------------------------------------------------
"""
def main():
    S, T = input().split()

    for w in range(1, len(S)):
        for c in range(w):
            if S[c::w] == T:
                print("Yes")
                return
    print("No")

if __name__ == "__main__":
    main()