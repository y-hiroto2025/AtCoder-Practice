"""
問題URL: https://atcoder.jp/contests/abc155/tasks/abc155_c
----------------------------------------------------
結果
・自力（10min）
----------------------------------------------------
"""
import sys
import collections

input = sys.stdin.readline

def main():
    N = int(input())
    S = [input().strip() for _ in range(N)]
    s_count = collections.Counter(S)
    
    max_count = s_count.most_common(1)[0][1]
    ans = [k for k, v in s_count.items() if v == max_count]

    ans.sort()

    print("\n".join(ans))

if __name__ == "__main__":
    main()