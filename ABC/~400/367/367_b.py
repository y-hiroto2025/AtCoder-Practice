"""
問題URL: https://atcoder.jp/contests/abc367/tasks/abc367_b
----------------------------------------------------
結果: 自力（5min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    X = input().strip()
    ans = X.rstrip("0").rstrip(".")
    print(ans)


if __name__ == "__main__":
    main()