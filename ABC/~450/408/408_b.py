"""
問題URL: https://atcoder.jp/contests/abc408/tasks/abc408_b
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))

    print(len(set(A)))
    print(*sorted(set(A)))



if __name__ == "__main__":
    main()