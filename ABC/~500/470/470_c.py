"""
問題URL: https://atcoder.jp/contests/abc470/tasks/abc470_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, Q = map(int, input().split())
    A = [0]*N
    idxs = []
    ans = 0

    for _ in range(Q):
        query = list(map(int, input().split()))

        if query[0] == 1:
            x = query[1]-1
            if A[x] == 0:
                idxs.append(x)

            ans ^= A[x] ^ (A[x] + 1)
            A[x] += 1

        else:
            for v in idxs:
                ans ^= A[v] ^ (A[v] - 1)
                A[v] -= 1

            idxs = [v for v in idxs if A[v] != 0]

        print(ans)
        

if __name__ == "__main__":
    main()