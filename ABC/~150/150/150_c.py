"""
問題URL: https://atcoder.jp/contests/abc150/tasks/abc150_c
----------------------------------------------------
結果
・7min
----------------------------------------------------
"""
import sys
from itertools import permutations

input = sys.stdin.readline

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))

    perms = list(permutations(range(1, N+1)))

    for i in range(len(perms)):

        if list(perms[i]) == P:
            p = i

        if list(perms[i]) == Q:
            q = i

    print(abs(p-q))


if __name__ == "__main__":
    main()