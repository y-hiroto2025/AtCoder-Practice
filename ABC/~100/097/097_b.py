"""
問題URL: https://atcoder.jp/contests/abc097/tasks/abc097_b
----------------------------------------------------
結果
・7min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    X = int(input())

    ans = 1

    for b in range(2, X+1):

        p = 2
        while b**p <= X:
            ans = max(ans, b**p)

            p += 1

    print(ans)


if __name__ == "__main__":
    main()