"""
問題URL: https://atcoder.jp/contests/abc113/tasks/abc113_b
----------------------------------------------------
結果
・4min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))

    ans_idx = 0
    min_diff = float('inf')

    for i in range(N):
        diff = abs((T - H[i]*0.006) - A)

        if diff < min_diff:
            min_diff = diff
            ans_idx = i+1

    print(ans_idx)

if __name__ == "__main__":
    main()