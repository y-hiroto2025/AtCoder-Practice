"""
問題URL: https://atcoder.jp/contests/abc413/tasks/abc413_c
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

input = sys.stdin.readline

def main():
    A = []
    Q = int(input())

    real_first = 0
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            c = query[1]
            x = query[2]
            A += [x] * c

        else:
            k = query[1]
            real_first += k - 1
            print(sum(A[real_first:]))
        print(A)


if __name__ == "__main__":
    main()