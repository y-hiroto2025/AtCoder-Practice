"""
問題URL: https://atcoder.jp/contests/abc328/tasks/abc328_b
----------------------------------------------------
結果
・自力（15min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    D = list(map(int, input().split()))

    ans = 0

    for i in range(N):
        for d in range(1, D[i] + 1):
            i_d_str = str(i + 1) + str(d)
            """if str(i + 1)[0] * len(i_d_str) == i_d_str:
                ans += 1"""
            if len(set(i_d_str)) == 1:
                ans += 1

    print(ans)

if __name__ == "__main__":
    main()