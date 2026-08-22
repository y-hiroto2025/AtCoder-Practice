"""
問題URL: https://atcoder.jp/contests/abc114/tasks/abc114_b
----------------------------------------------------
結果
・4min
----------------------------------------------------
"""
def main():
    S = input().strip()
    ans = float('inf')

    for i in range(len(S)-2):
        ans = min(ans, abs(753 - int(S[i:i+3])))

    print(ans)

if __name__ == "__main__":
    main()