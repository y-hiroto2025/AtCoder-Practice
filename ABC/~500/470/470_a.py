"""
問題URL: https://atcoder.jp/contests/abc470/tasks/abc470_a
----------------------------------------------------
結果
・1min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    for i in range(1, N+1):
        if i % 3 == 0:
            print("Fizz")
        else:
            print(i)


if __name__ == "__main__":
    main()