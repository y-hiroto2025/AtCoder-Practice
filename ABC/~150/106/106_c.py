"""
問題URL: https://atcoder.jp/contests/abc106/tasks/abc106_c
----------------------------------------------------
結果
・4min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    S = input().strip()
    K = int(input())

    for i in range(len(S)):
        if S[i] != '1':
            print(S[i])
            return

        elif i+1 == K:
            print(1)
            return


if __name__ == "__main__":
    main()