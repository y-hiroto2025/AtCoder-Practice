"""
問題URL: https://atcoder.jp/contests/abc073/tasks/abc073_b
----------------------------------------------------
結果
・自力（5min）

解法ポイント、学び
・
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    num = int(input())
    ans = 0

    for _ in range(num):
        l_i, r_i = map(int, input().split())
        ans += (r_i - l_i + 1)
    
    print(ans)

if __name__ == "__main__":
    main()