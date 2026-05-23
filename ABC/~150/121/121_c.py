"""
問題URL: https://atcoder.jp/contests/abc121/tasks/abc121_c
----------------------------------------------------
結果
・自力（7min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())

    drinks = []
    for _ in range(N):
        a, b = map(int, input().split())

        drinks.append((a, b))
    
    drinks_sorted = sorted(drinks)

    ans = 0
    for i in range(N):
        a = drinks_sorted[i][0]
        b = drinks_sorted[i][1]

        if M - b > 0:
            M -= b
            ans += a * b
        else:
            ans += a * M

            print(ans)
            return


if __name__ == "__main__":
    main()