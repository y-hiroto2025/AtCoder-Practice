"""
問題URL: https://atcoder.jp/contests/arc036/tasks/arc036_a
----------------------------------------------------
結果
・自力（4min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    t = []

    ans = -1
    for i in range(N):
        t.append(int(input()))

        if sum(t[-3:]) < K:
            ans = i + 1
            break
    
    print(ans)


if __name__ == "__main__":
    main()