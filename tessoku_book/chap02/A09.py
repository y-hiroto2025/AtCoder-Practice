# ２次元累積和
import sys
input = sys.stdin.readline

def main():
    H, W, N = map(int, input().split())
    mass = [[0] * (W + 2) for _ in range(H + 2)]

    for _ in range(N):
        A, B, C, D = map(int, input().split())
        mass[A][B] += 1
        mass[C+1][D+1] += 1
        mass[C+1][B] -= 1
        mass[A][D+1] -= 1
        
    # 横方向に累積
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            mass[i][j] += mass[i][j-1]
    
    # 縦方向に累積
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            mass[i][j] += mass[i-1][j]

    for i in range(1, H + 1):
        print(*mass[i][1:W+1])

if __name__ == "__main__":
    main()