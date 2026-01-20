"""
問題URL: https://atcoder.jp/contests/abc364/tasks/abc364_b
----------------------------------------------------
結果
・ギブアップ
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    H, W = map(int, input().split())
    S_i, S_j = map(int, input().split())
    C = []

    now_i = S_i - 1
    now_j = S_j - 1

    for _ in range(H):
        C.append(input().strip())

    X = input().strip()

    for x in X:
        move_i = 0
        move_j = 0

        if x == "L":
            move_j = -1
        elif x == "R":
            move_j = 1
        elif x == "U":
            move_i = -1
        else:
            move_i = 1
        
        if 0 <= now_i + move_i < H and 0 <= S_j + move_j < W:
            if C[now_i + move_i][now_j + move_j] == ".":
                now_i += move_i
                now_j += move_j
        
    print(now_j + 1, now_j + 1)


if __name__ == "__main__":
    main()