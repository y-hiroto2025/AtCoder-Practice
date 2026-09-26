"""
url: https://atcoder.jp/contests/code-festival-2016-quala/tasks/codefestival_2016_qualA_b
"""

import sys

input = sys.stdin.readline

def main():
    N = int(input())
    a = list(map(int, input().split()))

    pairs_set = set()
    ans = 0

    for i in range(N):
        pairs_set.add((i+1, a[i]))

        if (a[i], i+1) in pairs_set:
            ans += 1

    print(ans)
    
    
if __name__ == "__main__":
    main()