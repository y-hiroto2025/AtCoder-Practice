"""
問題URL: https://atcoder.jp/contests/abc289/tasks/abc289_b
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    a = set(map(int, input().split()))

    stack = []

    for i in range(1, N + 1):
        stack.append(i)

        if i not in a:
            print(*stack[::-1], end=" ")

            stack = []
    print()

if __name__ == "__main__":
    main()