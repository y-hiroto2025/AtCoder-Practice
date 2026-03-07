"""
問題URL: https://atcoder.jp/contests/abc278/tasks/abc278_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, Q = map(int, input().split())

    folow = set()

    for _ in range(Q):
        T, A, B = map(int, input().split())

        if T == 1:      # AがBをフォロー
            folow.add((A, B))
        
        elif T == 2:    # AがBを解除
            folow.discard((A, B))
        
        else:           # AとBがFFの場合Yes
            if (A, B) in folow and (B, A) in folow:
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    main()