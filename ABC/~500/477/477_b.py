"""
問題URL: https://atcoder.jp/contests/abc477/tasks/abc477_b
----------------------------------------------------
結果
・5min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, D = map(int, input().split())
    X = list(map(int, input().split()))
    ans_list = []

    for i in range(N):
        cnt = 0

        for j in range(N):

            if abs(X[i] - X[j]) >= D and i != j:
                cnt += 1

        if cnt == N-1:
            ans_list.append(i+1)

    print(len(ans_list))
    print(*sorted(ans_list))


if __name__ == "__main__":
    main()