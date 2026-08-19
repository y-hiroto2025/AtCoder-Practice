"""
問題URL: https://atcoder.jp/contests/abc142/tasks/abc142_c
----------------------------------------------------
結果
・3min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans_list = [0]*N

    for i in range(N):
        ans_list[A[i]-1] = i+1

    print(*ans_list)


if __name__ == "__main__":
    main()