"""
問題URL: https://atcoder.jp/contests/abc156/tasks/abc156_c
----------------------------------------------------
結果
・自力（6min）

解法ポイント、学び
・２乗和の合計が最小になるのは平均値。
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    X = list(map(int, input().split()))
    """current_min = float('inf')

    for p in range(min(X), max(X) + 1):
        consumption = sum((x - p)**2 for x in X)

        current_min = min(current_min, consumption)

    print(current_min)"""

    avg = sum(X) / N
    P = int(avg + 0.5) # 四捨五入
    ans = sum((x - P) ** 2 for x in X)
    print(ans)
    
if __name__ == "__main__":
    main()