"""
問題URL: https://atcoder.jp/contests/abc422/tasks/abc422_b
----------------------------------------------------
結果
・自力（14min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    H, W = map(int, input().split())

    S = [input().strip() for _ in range(H)]

    for i in range(H):
        for j in range(W):
            cnt = 0

            if S[i][j] == "#":

                if i != H-1:
                    if S[min(i+1, H)][j] == "#":
                        cnt += 1
                if j != W-1:
                    if S[i][min(j+1, W)] == "#":
                        cnt += 1
                if S[max(0, i-1)][j] == "#" and i != 0:
                    cnt += 1
                if S[i][max(0, j-1)] == "#" and j != 0:
                    cnt += 1
            else:
                continue
        
            if cnt != 2 and cnt != 4:
                print("No")
                return
    
    print("Yes")


if __name__ == "__main__":
    main()