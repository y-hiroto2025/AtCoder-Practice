# 二次元DP: ナップザック問題
import sys
input = sys.stdin.readline

def main():
    N, W_limit = map(int, input().split())

    weight = []
    value = []
    for _ in range(N):
        w, v = map(int, input().split())
        weight.append(w)
        value.append(v)
    
    dp = [[-1] * (W_limit + 1) for _ in range(N + 1)]

    dp[0][0] = 0

    for i in range(1, N + 1):
        w_i



if __name__ == "__main__":
    main()