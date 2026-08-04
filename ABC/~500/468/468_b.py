"""
問題URL: https://atcoder.jp/contests/abc468/tasks/abc468_b
----------------------------------------------------
結果
・10min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    M, D = map(int, input().split())
    S = input().strip()

    observed_mass = set()

    for i in range(M):

        if S[i] == "G":

            for m in range(max(0, i-D), min(M-1, i+D)+1):
                observed_mass.add(m)

    ans = sum([1 for i in range(M) if i not in observed_mass])
    print(ans)


if __name__ == "__main__":
    main()