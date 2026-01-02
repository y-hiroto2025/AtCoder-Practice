"""
問題URL: https://atcoder.jp/contests/abc342/tasks/abc342_b
----------------------------------------------------
結果
・自力（7min）

解法ポイント、学び
・
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    P = list(map(int, input().split()))

    posision = {person: i for i, person in enumerate(P)}

    Q = int(input())
    for i in range(Q):
        A_i, B_i = map(int, input().split())
        """front = min(P.index(A_i), P.index(B_i))
        print(P[front])時間がかかる"""

        if posision[A_i] < posision[B_i]:
            print(A_i)
        else:
            print(B_i)



if __name__ == "__main__":
    main()