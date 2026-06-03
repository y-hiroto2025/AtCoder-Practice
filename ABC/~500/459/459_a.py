"""
問題URL: https://atcoder.jp/contests/abc459/tasks/abc459_a
----------------------------------------------------
結果
・
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    X = int(input())
    s = "HelloWorld"

    print(s[:X-1] + s[X:])


if __name__ == "__main__":
    main()