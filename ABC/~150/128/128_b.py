"""
問題URL: https://atcoder.jp/contests/abc128/tasks/abc128_b
----------------------------------------------------
結果
・11min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())

    ans_dict = {}

    for i in range(N):
        s, p = input().split()
        p = int(p)

        if s in ans_dict:
            ans_dict[s].append((p, i))
        else:
            ans_dict[s] = [(p, i)]

    ans_dict = dict(sorted(ans_dict.items()))

    for key, values in ans_dict.items():
        values = sorted(values, reverse=True)

        for val in values:
            print(val[1]+1)


if __name__ == "__main__":
    main()