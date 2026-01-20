"""
問題URL: https://atcoder.jp/contests/abc306/tasks/abc306_c
----------------------------------------------------
結果
・

なぜ解けなかった？
・

解法ポイント、学び
・
----------------------------------------------------
"""
import sys
from collections import Counter
input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    i_dict = {i: 0 for i in range(N)}

    for i in range(N * 3):
        i_dict[i] += 1
        if i_dict[i] == 2:
            print(i)

if __name__ == "__main__":
    main()