"""
問題URL: https://atcoder.jp/contests/abc325/tasks/abc325_b
----------------------------------------------------
解法ポイント、学び
・
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    W = []
    X = []
    for i in range(N):
        W_i, X_i = map(int, input().split())
        W.append(W_i)
        X.append(X_i)

    ans = 0    
    for time in range(24):
        current_ans = 0

        for i in range(N):
            time_i = (X[i] + time) % 24

            if time_i >= 9 and time_i < 18:
                current_ans += W[i]

        ans = max(ans, current_ans)

    print(ans)

if __name__ == "__main__":
    main()