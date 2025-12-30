"""
問題URL: https://atcoder.jp/contests/abc332/tasks/abc332_b
----------------------------------------------------
結果
・自力（12min）
----------------------------------------------------
"""
def main():
    K, G, M = map(int, input().split())
    glass = 0
    cup = 0

    for _ in range(K):
        if glass == G:
            glass = 0

        elif cup == 0:
            cup = M

        else:
            """glass, cup = min(G, glass + cup), max(0, cup - (G - glass))"""
            move_amount = min(cup, G - glass)

            glass += move_amount
            cup -= move_amount
    
    print(glass, cup)


if __name__ == "__main__":
    main()