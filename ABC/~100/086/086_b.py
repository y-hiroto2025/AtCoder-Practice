"""
問題URL: https://atcoder.jp/contests/abc086/tasks/abc086_b
----------------------------------------------------
結果
・3min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    a, b = map(str, input().split())
    num = int(a + b)

    for i in range(num//2):
        if i**2 == num:
            print("Yes")
            return

    print("No")


if __name__ == "__main__":
    main()