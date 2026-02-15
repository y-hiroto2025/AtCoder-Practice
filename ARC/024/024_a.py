"""
問題URL: https://atcoder.jp/contests/arc024/tasks/arc024_1
----------------------------------------------------
----------------------------------------------------
"""
import sys
from collections import Counter

input = sys.stdin.readline

def main():
    L, R = map(int, input().split())
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))

    count_l = Counter(l)
    count_r = Counter(r)

    ans = 0

    for size in count_l.keys():
        if size in count_r:
            ans += min(count_l[size], count_r[size])

    print(ans)


if __name__ == "__main__":
    main()