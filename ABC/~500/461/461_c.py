"""
問題URL: https://atcoder.jp/contests/abc461/tasks/abc461_c
----------------------------------------------------
結果
・自力（19min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, K, M = map(int, input().split())

    jewel = []
    for _ in range(N):
        c, v = map(int, input().split())
        jewel.append((c, v))
    
    jewel.sort(key=lambda x: x[1], reverse=True)

    first_jewels = []
    other_jewels = []
    color_set = set()

    for c, v in jewel:
        if c not in color_set:
            color_set.add(c)
            first_jewels.append(v)
        else:
            other_jewels.append(v)
    
    ans = 0

    ans += sum(first_jewels[:M])
    remains = sorted(first_jewels[M:] + other_jewels, reverse=True)

    ans += sum(remains[:K-M])

    print(ans)


if __name__ == "__main__":
    main()