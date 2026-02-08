# ２次元累積和
import sys
input = sys.stdin.readline

def main():
    H, W = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(H)]

    prefix = [[0] * (W + 1) for _ in range(H + 1)]
    for i in range(H):
        for j in range(W):
            prefix[i+1][j+1] = X[i][j]

    # 横方向に累積
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            prefix[i][j] += prefix[i][j-1]
    
    # 縦方向に累積
    for j in range(1, W + 1):
        for i in range(1, H + 1):
            prefix[i][j] += prefix[i-1][j]

    Q = int(input())
    for i in range(Q):
        A, B, C, D = map(int, input().split())
        ans = prefix[C][D] - prefix[C][B-1] - prefix[A-1][D] + prefix[A-1][B-1]
        print(ans)


if __name__ == "__main__":
    main()