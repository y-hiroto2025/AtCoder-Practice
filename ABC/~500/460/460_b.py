"""
問題URL: https://atcoder.jp/contests/abc460/tasks/abc460_b
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    T = int(input())

    for _ in range(T):
        X_1, Y_1, R_1, X_2, Y_2, R_2 = map(int, input().split())

        if (R_1 - R_2) ** 2 <= (X_1 - X_2) ** 2 + (Y_1 - Y_2) ** 2 <= (R_1 + R_2) ** 2:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()