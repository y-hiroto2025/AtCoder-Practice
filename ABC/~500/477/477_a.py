"""
問題URL: https://atcoder.jp/contests/abc477/tasks/abc477_a
----------------------------------------------------
結果
・1min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    c = input().strip()

    if c=="B":
        print("Y")
    elif c=="Y":
        print("R")
    elif c=="R":
        print("B")


if __name__ == "__main__":
    main()