# 動的計画法2(最短ルート)
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    dp = [0, A[0]]
    for i in range(2, N):
        dp.append(min(dp[i-1] + A[i-1], dp[i-2] + B[i-2]))
    
    P = []
    current = N - 1
    while True:
        P.append(current + 1)   # 現在の位置を追加
        if current == 0:        # 最初の一に戻ったら終わり
            break
        
        # 一つ前の部屋への最短時間==そこからの移動時間
        if dp[current] == dp[current-1] + A[current-1]:
            current -= 1
        else:
            current -= 2
    
    P.reverse()

    print(len(P))
    print(*P)

if __name__ == "__main__":
    main()