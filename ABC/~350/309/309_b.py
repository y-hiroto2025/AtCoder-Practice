"""
問題URL: 
----------------------------------------------------
結果
・ギブアップ

なぜ解けなかった？
・一つのマスリストで数字を動かそうとしていた

解法ポイント、学び
・新しいリストに数字を映していく
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    masu = [input().strip() for _ in range(N)]
    masu_new = [list(row) for row in masu]

    # 上の辺
    for j in range(N - 1):
        masu_new[0][j + 1] = masu[0][j]
    
    # 右の辺
    for i in range(N - 1):
        masu_new[i + 1][N - 1] = masu[i][N - 1]

    # 下の辺
    for j in range(N - 1):
        masu_new[N - 1][j] = masu[N - 1][j + 1]
    
    # 左の辺
    for i in range(N - 1):
        masu_new[i][0] = masu[i + 1][0]

    print()
    for row in masu_new:
        print("".join(row))


if __name__ == "__main__":
    main()