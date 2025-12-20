"""
問題URL: https://atcoder.jp/contests/abc348/tasks/abc348_c
----------------------------------------------------
結果
・自力（15min）

解法ポイント、学び
・
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    bean_dic = {}

    for _ in range(N):
        taste_i, color_i = map(int, input().split())
        if not color_i in bean_dic:
            bean_dic[color_i] = taste_i
        else:
            if bean_dic[color_i] > taste_i:
                bean_dic[color_i] = taste_i
    bean_values = list(bean_dic.values())
    print(max(bean_values))


if __name__ == "__main__":
    main()