"""
問題URL: https://atcoder.jp/contests/abc109/tasks/abc109_b
----------------------------------------------------
結果
・5min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())

    word_set = set()

    pre_W = input().strip()
    word_set.add(pre_W)
    ans = "Yes"

    for _ in range(N-1):
        W = input().strip()

        if W in word_set or W[0] != pre_W[-1]:
            ans = "No"

        pre_W = W
        word_set.add(W)

    print(ans)


if __name__ == "__main__":
    main()