"""
問題URL: https://atcoder.jp/contests/abc358/tasks/abc358_c
----------------------------------------------------
----------------------------------------------------
"""
import sys
import itertools

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    for x in range(1, N + 1):
        comb = list(itertools.combinations(S, x))

        for c in comb:
            tasets = set()

            for market in c:
                for j in range(M):
                    if market[j] == "o":
                        tasets.add(j)
            
            if len(tasets) == M:
                print(x)
                return


if __name__ == "__main__":
    main()