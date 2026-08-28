"""
問題URL: https://atcoder.jp/contests/abc095/tasks/arc096_a
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    A,B,C,X,Y = map(int, input().split())

    p1 = A*X + B*Y

    ab_cnt = min(X,Y) * 2
    rem_x = max(0, X - ab_cnt // 2)
    rem_y = max(0, Y - ab_cnt // 2)
    p2 = C * ab_cnt + A*rem_x + B*rem_y

    p3 = C * max(X, Y) * 2

    print(min(p1,p2,p3))


if __name__ == "__main__":
    main()