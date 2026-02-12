# 動的計画法1(最短時間)
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    dp = [0, A[0]]
    for i in range(2, N):
        route1 = dp[i-1]+A[i-1]
        route2 = dp[i-2]+B[i-2]
        dp.append(min(route1, route2))

    print(dp[N-1])


if __name__ == "__main__":
    main()