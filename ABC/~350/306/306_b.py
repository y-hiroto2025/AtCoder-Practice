"""
問題URL: https://atcoder.jp/contests/abc306/tasks/abc306_b
----------------------------------------------------
結果
・自力（5min）

解法ポイント、学び
・２の乗算はビットシフトを使うと速い
・pythonではintで2進数を10進数に変換できる
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    a = list(map(int, input().split()))
    ans = 0

    for i in range(64):
        ans += a[i] * (2**i)

    print(ans)

    """
    ビットシフト演算
    ans += a[i] * (2**i)
    を
    if a[i] == 1:
        ans += (1 << i) (1 << 0: 1*(2**0), 1 << 1: 2*(2**1))
    にするとはやい
    """

if __name__ == "__main__":
    main()