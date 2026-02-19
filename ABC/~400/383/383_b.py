"""
問題URL: https://atcoder.jp/contests/abc383/tasks/abc383_b
----------------------------------------------------
----------------------------------------------------
"""
import sys
import itertools

input = sys.stdin.readline

def main():
    H, W, D = map(int, input().split())
    S = [input().strip() for _ in range(H)]

    floors = []
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                floors.append((i, j))
    
    ans = 0
    for (r1, c1), (r2, c2) in itertools.combinations(floors, 2):
        count_c = 0

        for r, c in floors:
            cond1 = abs(r1-r) + abs(c1-c) <= D
            cond2 = abs(r2-r) + abs(c2-c) <= D
            
            if cond1 or cond2:
                count_c += 1

        ans = max(ans, count_c)
    
    print(ans)


if __name__ == "__main__":
    main()