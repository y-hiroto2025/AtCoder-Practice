"""
問題URL: https://atcoder.jp/contests/abc120/tasks/abc120_b
----------------------------------------------------
結果
・自力で解いた（6min）

解法ポイント、学び
・
----------------------------------------------------
"""
import math
def main():
    A, B, K = map(int, input().split())
    count = 0

    gcd = math.gcd(A, B)

    for i in range(gcd, 0, -1):
        # if (A % i == 0) and (B % i == 0):
        if gcd % i == 0: # iがgcdの約数<=>AとB両方の約数
        # 計算は一回で済むのでこの方が良い
            count += 1
        if count == K:
            print(i)
            break
    """
    内包表記を使えばシンプルになる
    g = math.gcd(A, B)
    common_divisors = [i for i in range(1, g + 1) if g % i == 0]
    print(common_divisors[-K])
    """

if __name__ == "__main__":
    main()