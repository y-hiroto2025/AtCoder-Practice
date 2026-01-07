"""
問題URL: https://atcoder.jp/contests/abc358/tasks/abc358_b
----------------------------------------------------
結果
・自力（8min）

解法ポイント、学び
・
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, A = map(int, input().split())
    T = list(map(int, input().split()))
    current_time = 0

    """for i in range(len(T)):"""
    for t in T:
        """if T[i] <= current_time:
            current_time += A
        else:
            current_time = A + T[i]"""
        current_time = max(current_time, T[i]) + A
        print(current_time)

if __name__ == "__main__":
    main()