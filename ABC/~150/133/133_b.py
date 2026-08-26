"""
問題URL: https://atcoder.jp/contests/abc133/tasks/abc133_b
----------------------------------------------------
結果
・5min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, D = map(int, input().split())
    X = []
    ans = 0

    for _ in range(N):
        X.append(list(map(int, input().split())))

    for i in range(N-1):
        for j in range(i+1, N):

            diff_float = sum((X[i][d]-X[j][d])**2 for d in range(D))**0.5
            diff_int = int(diff_float)

            if diff_float == diff_int:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()