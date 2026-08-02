"""
問題URL: https://atcoder.jp/contests/abc466/tasks/abc466_b
----------------------------------------------------
結果
・5min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())

    ball_list = [-1] * M

    C_S = []

    for _ in range(N):
        c, s = map(int, input().split())
        C_S.append((c, s))

    C_S = sorted(C_S)

    for i in range(N):
        c = C_S[i][0]
        s = C_S[i][1]
        ball_list[c-1] = max(ball_list[c-1], s)

    print(*ball_list)

if __name__ == "__main__":
    main()