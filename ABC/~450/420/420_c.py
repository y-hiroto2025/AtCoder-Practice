"""
問題URL: https://atcoder.jp/contests/abc420/tasks/abc420_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    min_sum = [min(A[i], B[i]) for i in range(N)]
    ans = sum(min_sum)

    for _ in range(Q):
        c, X, V = input().split()
        X = int(X) - 1
        V = int(V)

        old_min = min(A[X], B[X])

        if c == "A":
            A[X] = V
        else:
            B[X] = V
        
        new_min = min(A[X], B[X])

        ans += new_min - old_min
        
        print(ans)


if __name__ == "__main__":
    main()