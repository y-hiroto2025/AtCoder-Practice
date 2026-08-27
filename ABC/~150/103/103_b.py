"""
問題URL: https://atcoder.jp/contests/abc103/tasks/abc103_b
----------------------------------------------------
結果
・4min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    S = input().strip()
    T = input().strip()

    for _ in range(len(S)):
        if S == T:
            print("Yes")
            return

        S = S[-1] + S[:-1]

    print("No")

if __name__ == "__main__":
    main()