"""
問題URL: https://atcoder.jp/contests/abc464/tasks/abc464_b
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    H, W = map(int, input().split())
    C = []

    top, bottom = 0, H
    left, right = 0, W

    for _ in range(H):
        c = input().strip()
        C.append(c)
    
    first = True
    
    for i in range(H):
        for j in range(W):

            if C[i][j] == "#":
                if first:
                    first = False
                    top, bottom = i, i
                    left, right = j, j

                top = min(top, i)
                bottom = max(bottom, i)
                left = min(left, j)
                right = max(right, j)
    
    for i in range(top, bottom+1):
        print(C[i][left:right+1])
    

if __name__ == "__main__":
    main()