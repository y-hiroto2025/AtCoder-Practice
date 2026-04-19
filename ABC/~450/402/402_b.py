"""
問題URL: https://atcoder.jp/contests/abc402/tasks/abc402_b
----------------------------------------------------
結果
・自力（3min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    Q = int(input())

    orders = []

    for _ in range(Q):
        querry = list(map(int, input().split()))

        if querry[0] == 1:
            orders.append(querry[1])
        else:
            print(orders.pop(0))


if __name__ == "__main__":
    main()