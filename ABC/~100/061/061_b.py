"""
問題URL: https://atcoder.jp/contests/abc061/tasks/abc061_b
----------------------------------------------------
結果
・3min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())

    ans_list = [0]*N

    for _ in range(M):
        a, b = map(int, input().split())

        ans_list[a-1] += 1
        ans_list[b-1] += 1

    print(*ans_list, sep="\n")


if __name__ == "__main__":
    main()