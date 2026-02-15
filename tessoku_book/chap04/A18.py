# 2次元DP: 部分和
import sys
input = sys.stdin.readline

def main():
    N, S = map(int, input().split())
    A = list(map(int, input().split()))

    # i枚目までのカードを使って合計jを作れるかどうか
    dp = [[False] * (S + 1) for _ in range(N + 1)]

    dp[0][0] = True # 0は作れる

    for i in range(1, N + 1):
        card_val = A[i - 1]

        for j in range(S + 1):
            # 上の行がTrueなら今回もTrue
            if dp[i - 1][j] is True:
                dp[i][j] = True
            
            # j-カード の数字が以前作れて、jがカードの数字より大きいなら 足せばjになる
            elif j >= card_val and dp[i - 1][j - card_val] is True:
                dp[i][j] = True
            
            """
            if j < card_val:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] (もしくは dp[i - 1][i - card_val])
            """

    if dp[N][S]:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()