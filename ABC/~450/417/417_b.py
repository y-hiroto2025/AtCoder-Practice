"""
問題URL: https://atcoder.jp/contests/abc417/tasks/abc417_b
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    for i in range(M):
        if B[i] in A:
            A.remove(B[i])
    
    if A != []:
        print(*A)

if __name__ == "__main__":
    main()