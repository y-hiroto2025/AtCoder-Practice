# 二次元DP: ナップサック問題
import sys
input = sys.stdin.readline

def main():
    N, W = map(int, input().split())

    weights = []
    values = []
    for _ in range(N):
        w, v = map(int, input().split())
        weights.append(w)
        values.append(v)
    
    dp = [[0] * (W + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        weight = weights[i - 1]
        value = values[i - 1]

        for j in range(W + 1):
            if j < weight:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
    
    print(dp[N][W])


if __name__ == "__main__":
    main()