"""
問題URL: https://atcoder.jp/contests/abc053/tasks/abc053_b
----------------------------------------------------
結果
・2min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    s = input().strip().lower()

    first_idx = len(s)
    end_idx = 0

    for i in range(len(s)):

        if s[i] == "a":
            first_idx = min(first_idx, i)
        elif s[i] == "z":
            end_idx = max(end_idx, i)

    print(end_idx - first_idx + 1)


if __name__ == "__main__":
    main()