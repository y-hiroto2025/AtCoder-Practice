"""
問題URL: https://atcoder.jp/contests/abc434/tasks/abc434_b
----------------------------------------------------
結果
・自力（4min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    bards = {}

    for _ in range(N):
        a, b = map(int, input().split())
        if a in bards:
            bards[a].append(b)
        else:
            bards[a] = [b]
    
    for k in range(M):
        print(sum(bards[k+1]) / len(bards[k+1]))


if __name__ == "__main__":
    main()