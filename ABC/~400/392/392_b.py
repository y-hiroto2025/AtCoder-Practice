"""
問題URL: https://atcoder.jp/contests/abc392/tasks/abc392_b
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    A = set(map(int, input().split()))

    num_set = set([i for i in range(1, N + 1)])
    ans = num_set - A

    print(len(ans))
    print(*sorted(ans))


if __name__ == "__main__":
    main()