"""
問題URL: https://atcoder.jp/contests/abc471/tasks/abc471_a
----------------------------------------------------
結果
・1min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    a,b = map(int, input().split())

    if (a+b==9)or(a-b==9)or(a*b==9)or(a/b==9.0):
        print("Nine")
    else:
        print("Nein")


if __name__ == "__main__":
    main()