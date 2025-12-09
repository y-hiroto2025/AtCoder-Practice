"""
問題URL: https://atcoder.jp/contests/abc112/tasks/abc112_b
----------------------------------------------------
結果
・自力（10min）

解法ポイント、学び
・空リストはFalseとみなされる
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    n, t = map(int, input().split())
    c = []
    for _ in range(n):
        c_i, t_i = map(int, input().split())
        if t_i <= t:
            c.append(c_i)
    
    if c == []:
    # if not c: の方が良い（[]はFalseとみなされる）
        print("TLE")
    else:
        print(min(c))

if __name__ == "__main__":
    main()