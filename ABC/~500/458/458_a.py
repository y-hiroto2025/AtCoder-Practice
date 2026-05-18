"""
問題URL: https://atcoder.jp/contests/abc458/tasks/abc458_a
----------------------------------------------------
結果
・自力（0.4min）
----------------------------------------------------
"""

S = input().strip()
N = int(input())

print(S[N: len(S)-N])
