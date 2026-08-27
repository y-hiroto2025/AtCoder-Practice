"""
問題URL: https://atcoder.jp/contests/abc148/tasks/abc148_d
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    a = list(map(int, input().split()))

    target = 1
    for a_i in a:
        if a_i == target:
            target += 1

    if target == 1:
        print(-1)
    else:
        print(N - target+1)


if __name__ == "__main__":
    main()