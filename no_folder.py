"""
問題URL: https://atcoder.jp/contests/tenka1-2017-beginner/tasks/tenka1_2017_b
----------------------------------------------------
結果
・自力（10min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    point_dic = {}
    for _ in range(N):
        A_i, B_i = map(int, input().split())
        point_dic[B_i] = A_i
    min_point = min(point_dic)

    print(min_point + point_dic[min_point])


if __name__ == "__main__":
    main()