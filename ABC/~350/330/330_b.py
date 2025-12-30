"""
問題URL: https://atcoder.jp/contests/abc330/tasks/abc330_b
----------------------------------------------------
解法ポイント、学び
・
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))

    ans_list = []

    for a in A:
        if a < L:
            ans_list.append(L)
        
        elif L <= a and a <= R:
            ans_list.append(a)
        
        else:
            ans_list.append(R)
    print(*ans_list)


if __name__ == "__main__":
    main()