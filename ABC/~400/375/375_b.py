"""
問題URL: https://atcoder.jp/contests/abc375/tasks/abc375_b
----------------------------------------------------
結果
・自力（5min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())

    ans = 0
    curr_x = 0
    curr_y = 0

    for _ in range(N):
        x, y = map(int, input().split())
        cost = ((curr_x-x)**2 + (curr_y-y)**2) ** 0.5

        ans += cost
        curr_x = x
        curr_y = y

    ans += (curr_x**2 + curr_y**2) ** 0.5
    
    print(ans)


if __name__ == "__main__":
    main()