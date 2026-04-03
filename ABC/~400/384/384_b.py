"""
問題URL: https://atcoder.jp/contests/abc385/tasks/abc385_b
----------------------------------------------------
結果
・自力（4min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, R = map(int, input().split())

    for _ in range(N):
        d, a = map(int, input().split())
        
        if d == 1 and 1600 <= R and R <= 2799:
            R += a
        elif d == 2 and 1200 <= R and R <= 2399:
            R += a
    
    print(R)


if __name__ == "__main__":
    main()