"""
問題URL: https://atcoder.jp/contests/abc369/tasks/abc369_b
----------------------------------------------------
結果
・自力（13min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())

    last_r = 0
    last_l = 0
    ans = 0

    for i in range(N):
        a, s = input().split()
        a = int(a)
        if s == 'R':
            if last_r != 0:
                ans += abs(a - last_r)
            last_r = a

        else:
            if last_l != 0:
                ans += abs(a - last_l)
            last_l = a
    
    print(ans)


if __name__ == "__main__":
    main()