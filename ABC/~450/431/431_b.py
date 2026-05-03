"""
問題URL: https://atcoder.jp/contests/abc431/tasks/abc431_b
----------------------------------------------------
結果
・自力（5min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    X = int(input())
    N = int(input())
    W = list(map(int, input().split()))

    Q = int(input())
    equips = []
    
    for _ in range(Q):
        q = int(input()) - 1

        if q not in equips:
            equips.append(q)
            X += W[q]
        else:
            equips.remove(q)
            X -= W[q]
        
        print(X)


if __name__ == "__main__":
    main()