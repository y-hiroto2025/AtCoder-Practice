"""
問題URL: https://atcoder.jp/contests/abc181/tasks/abc181_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())

    X, Y = [], []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)

    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                if (Y[k]-Y[i])*(X[j]-X[i]) == (Y[j]-Y[i])*(X[k]-X[i]):
                    print("Yes")
                    return
    
    print("No")


if __name__ == "__main__":
    main()