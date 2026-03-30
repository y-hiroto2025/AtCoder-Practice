"""
問題URL: https://atcoder.jp/contests/abc374/tasks/abc374_b
----------------------------------------------------
結果
・自力（9min）
----------------------------------------------------
"""
def main():
    S = input().strip()
    T = input().strip()

    ans = 0

    for i in range(min(len(S), len(T))):
        if S[i] != T[i]:
            ans += i + 1
            break

        if (i == len(S)-1 and i != len(T)-1) or (i == len(T) - 1 and i != len(S)-1):
            ans += i + 2
            break
    
    print(ans)

if __name__ == "__main__":
    main()