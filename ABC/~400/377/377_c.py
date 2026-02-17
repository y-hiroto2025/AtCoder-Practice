"""
問題URL: https://atcoder.jp/contests/abc377/tasks/abc377_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    a, b = [], []
    bad_pos = set()

    for _ in range(M):
        i, j = map(int, input().split())
        a.append(i)
        b.append(j)

        bad_pos.add((i, j))

        if i+2 <= N and j+1 <= N:
            bad_pos.add((i+2, j+1))
        if i+1 <= N and j+2 <= N:
            bad_pos.add((i+1, j+2))
        if i-1 >= 1 and j+2 <= N:
            bad_pos.add((i-1, j+2))
        if i-2 >= 1 and j+1 <= N:
            bad_pos.add((i-2, j+1))
        if i-2 >= 1 and j-1 >= 1:
            bad_pos.add((i-2, j-1))
        if i-1 >= 1 and j-2 >= 1:
            bad_pos.add((i-1, j-2))
        if i+1 <= N and j-2 >= 1:
            bad_pos.add((i+1, j-2))
        if i+2 <= N and j-1 >= 1:
            bad_pos.add((i+2, j-1))
    
    ans = N*N - len(bad_pos)
    print(ans)


if __name__ == "__main__":
    main()