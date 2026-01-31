"""
問題URL: https://atcoder.jp/contests/abc262/tasks/abc262_b
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())

    conb = [[False] * N for _ in range(N)]

    for _ in range(M):
        U_i, V_i = map(int, input().split())
        conb[U_i - 1][V_i - 1] = True
        conb[V_i - 1][U_i - 1] = True
    
    ans = 0

    for a in range(N):
        for b in range(a + 1, N):
            for c in range(b + 1, N):
                if conb[a][b] and conb[b][c] and conb[c][a]:
                    ans += 1
    
    print(ans)

if __name__ == "__main__":
    main()