"""
問題URL: https://atcoder.jp/contests/abc351/tasks/abc351_c
----------------------------------------------------
結果
・自力（23min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    balls = []

    for i in range(N):
        balls.append(A[i])

        while len(balls) > 1 and balls[-2] == balls[-1]:
            if balls[-2] == balls[-1]:
                balls.pop(-1)
                balls[-1] += 1

    print(len(balls))


if __name__ == "__main__":
    main()