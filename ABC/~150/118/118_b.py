"""
問題URL: https://atcoder.jp/contests/abc118/tasks/abc118_b
----------------------------------------------------
結果
・4min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    food_list = [0]*M

    for _ in range(N):
        K_A = list(map(int, input().split()))
        K = K_A[0]
        A = K_A[1:]

        for i in range(K):
            food_list[A[i]-1] += 1

    ans = 0
    for i in range(M):
        if food_list[i] == N:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()