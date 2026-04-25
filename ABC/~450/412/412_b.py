"""
問題URL: https://atcoder.jp/contests/abc412/tasks/abc412_b
----------------------------------------------------
結果
・自力（5min）
----------------------------------------------------
"""
def main():
    S = input().strip()
    T = input().strip()

    if S[0].isupper():
        S = S[1:]

    for i in range(len(S)-1):
        if S[i+1].isupper():
            if S[i] not in T:
                print("No")
                return

    print("Yes")

if __name__ == "__main__":
    main()