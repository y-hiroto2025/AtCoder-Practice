"""
問題URL: https://atcoder.jp/contests/abc397/tasks/abc397_b
----------------------------------------------------
結果
・自力（7min）
----------------------------------------------------
"""
def main():
    S = input().strip()

    ans = 0
    first = 0

    if S[0] == "o":
        S = "i" + S
        ans += 1
        first += 1

    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            ans += 1
    
    if (len(S) + ans - first) % 2 != 0:
        ans += 1
        
    print(ans)


if __name__ == "__main__":
    main()