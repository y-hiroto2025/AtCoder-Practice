"""
問題URL: https://atcoder.jp/contests/abc020/tasks/abc020_b
----------------------------------------------------
結果
・自力（3min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    A, B = input().split()

    ans = int(A + B) * 2
    print(ans)


if __name__ == "__main__":
    main()