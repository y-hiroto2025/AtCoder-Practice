"""
問題URL: https://atcoder.jp/contests/abc429/tasks/abc429_c
----------------------------------------------------
----------------------------------------------------
"""
import sys
from collections import Counter

input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0

    num_count = Counter(A)
    for count in num_count.values():
        ans += (count*(count-1))//2 * (N-count)
    
    print(ans)


if __name__ == "__main__":
    main()