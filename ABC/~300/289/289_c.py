"""
問題URL: https://atcoder.jp/contests/abc289/tasks/abc289_c
----------------------------------------------------
----------------------------------------------------
"""
import sys
from itertools import combinations

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    A = []

    for _ in range(M):
        c = int(input())
        a = set(map(int, input().split()))
        A.append(a)
    
    ans = 0
    
    for k in range(1, M+1):
        comb = list(combinations(A, k))

        for c in comb:
            n = set().union(*c)
            
            if len(n) == N:
                ans += 1
    
    print(ans)


if __name__ == "__main__":
    main()