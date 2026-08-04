"""
問題URL: https://atcoder.jp/contests/abc468/tasks/abc468_c
----------------------------------------------------
結果
・12min
----------------------------------------------------
"""
import sys
from itertools import permutations
input = sys.stdin.readline

def main():
    N=int(input())
    P=list(map(int, input().split()))
    Q=list(map(int, input().split()))

    ans = 0

    for a in permutations([i+1 for i in range(N)]):
        ans += P < list(a) < Q

    print(ans)


if __name__ == "__main__":
    main()