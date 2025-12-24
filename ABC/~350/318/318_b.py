"""
問題URL: https://atcoder.jp/contests/abc318/tasks/abc318_b
----------------------------------------------------
結果
・自力（20min）

解法ポイント、学び
・
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    space = [[0] * 101 for _ in range(101)]
    ans = 0

    for _ in range(N):
        A, B, C, D = map(int, input().split())
        for y in range(C, D):
            for x in range(A, B):
                space[y][x] = 1
    
    """for y in range(101):
        ans += sum(space[y])"""
    ans = sum(sum(row) for row in space)
    print(ans)

if __name__ == "__main__":
    main()