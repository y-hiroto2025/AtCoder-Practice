"""
問題URL: 
----------------------------------------------------
結果
・

なぜ解けなかった？
・

解法ポイント、学び
・
----------------------------------------------------
"""
def main():
    A = [list(map(int, input().split())) for _ in range(4)]

    ans = "GAMEOVER"
    for i in range(3):
        for j in range(3):
            down = A[i + 1][j]
            right = A[i][j + 1]
            if A[i][j] == down or A[i][j] == right:
                ans = "CONTINUE"
                print(ans)
                return
    print(ans)

if __name__ == "__main__":
    main()