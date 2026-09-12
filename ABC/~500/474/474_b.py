"""
問題URL: https://atcoder.jp/contests/abc474/tasks/abc474_b
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    P = list(map(int, input().split()))

    cnt = 1

    for i in range(N):

        if P[i] > 10*cnt:
            print("No")
            return

        if i == 10*cnt - 1:
            cnt += 1

    print("Yes")


if __name__ == "__main__":
    main()