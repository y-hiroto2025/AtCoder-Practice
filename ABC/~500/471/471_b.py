"""
問題URL: https://atcoder.jp/contests/abc471/tasks/abc471_b
----------------------------------------------------
結果
・2min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())

    ans_list = {}

    for _ in range(N):
        s = input().strip().lower()

        if s in ans_list:
            ans_list[s] += 1
        else:
            ans_list[s] = 1

    print(max(ans_list.values()))


if __name__ == "__main__":
    main()