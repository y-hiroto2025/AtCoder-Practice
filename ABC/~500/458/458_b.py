"""
問題URL: https://atcoder.jp/contests/abc458/tasks/abc458_b
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    H, W = map(int, input().split())

    ans = [[0] * W for _ in range(H)]


    for i in range(H):
        for j in range(W):
            
            if i-1 >= 0:
                ans[i][j] += 1
            if i+1 < H:
                ans[i][j] += 1
            if j-1 >= 0:
                ans[i][j] += 1
            if j+1 < W:
                ans[i][j] += 1
    
    for i in range(H):
        print(*ans[i])


if __name__ == "__main__":
    main()