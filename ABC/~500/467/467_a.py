"""
問題URL: https://atcoder.jp/contests/abc467/tasks/abc467_a
----------------------------------------------------
結果
・1min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    H, W = map(int, input().split())
    BMI = W / H / H * 10000


    if BMI >= 25:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()