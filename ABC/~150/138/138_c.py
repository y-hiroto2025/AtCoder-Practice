"""
問題URL: https://atcoder.jp/contests/abc138/tasks/abc138_c
----------------------------------------------------
結果
・6min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    v = sorted(map(int, input().split()))


    for i in range(1, N):
        v[i] = (v[i]+v[i-1])/2

    print(v[-1])


if __name__ == "__main__":
    main()