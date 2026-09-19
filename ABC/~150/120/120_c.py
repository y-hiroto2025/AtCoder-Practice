"""
問題URL: https://atcoder.jp/contests/abc120/tasks/abc120_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    S = input().strip()
    zero_cnt = sum([1 for i in range(len(S)) if S[i] == "0"])

    ans = min(zero_cnt, len(S) - zero_cnt) * 2              

    print(ans)


if __name__ == "__main__":
    main()