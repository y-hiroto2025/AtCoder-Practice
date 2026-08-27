"""
問題URL: https://atcoder.jp/contests/abc058/tasks/abc058_b
----------------------------------------------------
結果
・3min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    O = input().strip()
    E = input().strip()

    for i in range(len(O)+len(E)):
        if i % 2 == 0:
            print(O[i//2], end="")
        else:
            print(E[i//2], end="")


if __name__ == "__main__":
    main()