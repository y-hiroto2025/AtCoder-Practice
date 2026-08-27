"""
問題URL: https://atcoder.jp/contests/abc049/tasks/abc049_b
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    H, W = map(int, input().split())

    for _ in range(H):
        C = input().strip()
        print(C)
        print(C)


if __name__ == "__main__":
    main()