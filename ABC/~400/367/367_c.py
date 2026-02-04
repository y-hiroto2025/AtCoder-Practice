"""
問題URL: https://atcoder.jp/contests/abc367/tasks/abc367_c
----------------------------------------------------
結果
・ギブアップ
----------------------------------------------------
"""
import sys
import itertools

input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    R = list(map(int, input().split()))

    ranges = [range(1, R[i] + 1) for i in range(N)]
    for comb in itertools.product(*ranges):
        if sum(comb) % K == 0:
            print(*comb)
            
if __name__ == "__main__":
    main()