"""
問題URL: https://atcoder.jp/contests/abc466/tasks/abc466_a
----------------------------------------------------
結果
・1min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    X = list(map(int, input().split()))
    for x in X:
        if x >= 0:
            print("No")
            return

    print("Yes")


if __name__ == "__main__":
    main()