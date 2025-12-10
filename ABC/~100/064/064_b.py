"""
問題URL: https://atcoder.jp/contests/abc064/tasks/abc064_b
----------------------------------------------------
結果
・自力（6min）

解法ポイント、学び
・端っこだけほしい=> max()やmin(), 順序が重要=> sort()やsorted()を使う
----------------------------------------------------
"""
def main():
    num_houses = int(input())
    house_coord = list(map(int, input().split()))
    # min_distance = 0
    # sorted_house_coord = sorted(house_coord) 無駄な計算
    # min_distance = sorted_house_coord[-1] - sorted_house_coord[0]

    ans = max(house_coord) - min(house_coord)
    print(ans)

if __name__ == "__main__":
    main()