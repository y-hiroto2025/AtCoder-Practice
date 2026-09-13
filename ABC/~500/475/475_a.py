"""
問題URL: https://atcoder.jp/contests/abc475/tasks/abc475_a
----------------------------------------------------
結果
・1min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    S = input().strip()

    for i in range(len(S)-1):
        print(S[i] + "o", end="")

    print(S[-1])


if __name__ == "__main__":
    main()