"""
問題URL: https://atcoder.jp/contests/abc474/tasks/abc474_a
----------------------------------------------------
結果
・1min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    X = int(input())
    num_list = [1, 2, 3]

    for num in num_list:
        if num != X:
            print(num)
            return


if __name__ == "__main__":
    main()