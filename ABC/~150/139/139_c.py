"""
問題URL: https://atcoder.jp/contests/abc139/tasks/abc139_c
----------------------------------------------------
結果
・7min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    H = list(map(int, input().split()))

    curr = 0
    ans = 0
    flg = False

    for i in range(N-1):

        if H[i]>=H[i+1]:
            if flg:
                curr += 1
            else:
                curr = 1
                flg = True
        else:
            if flg:
                flg = False
                ans = max(ans, curr)
                curr = 0

    ans = max(ans, curr)
    print(ans)


if __name__ == "__main__":
    main()