"""
問題URL: https://atcoder.jp/contests/abc356/tasks/abc356_b
----------------------------------------------------
結果
・自力（13min）

解法ポイント、学び
・
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ate = [0] * M

    """for _ in range(N):
        X_i = list(map(int, input().split()))
        for j in range(M):
            ate[j] += X_i[j]"""
    X = [list(map(int, input().split())) for _ in range(N)]

    ate = [sum(colum) for colum in zip(*X)]

    for j in range(M):
        if ate[j] < A[j]:
            print("No")
            return
    print("Yes")
    
if __name__ == "__main__":
    main()