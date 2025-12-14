"""
問題URL: https://atcoder.jp/contests/abc308/tasks/abc308_b
----------------------------------------------------
結果
・自力（15min）

解法ポイント、学び
・dictは存在チェックに加えて値の取り出しも速い
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    c = input().split() # 食べた皿の色(1~N)
    d = input().split() # 皿の色(1~M)
    p = list(map(int, input().split())) # 対応する値段(0~M)
    ans = 0

    # どれにも一致しないときの値段
    default_price = p[0]

    # keyとvalueｎ対応表を作る
    price_dict = {}
    for i in range(m):
        color = d[i]
        price = p[i + 1]
        price_dict[color] = price
    
    ans = 0
    for color in c:
        # get(key, デフォルト値)
        # キーがあればその値、なければデフォルト値を自動で返す
        ans += price_dict.get(color, default_price)
    
    print(ans)

if __name__ == "__main__":
    main()