"""
問題URL: https://atcoder.jp/contests/abc465/tasks/abc465_a
----------------------------------------------------
結果
・0.5min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    a, b = map(int, input().split())
    if 3*a > 2*b:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()