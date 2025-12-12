"""
問題URL: https://atcoder.jp/contests/abc305/tasks/abc305_b
----------------------------------------------------
結果 自力（10min）
・

解法ポイント、学び
・辞書を使って座標を決める方が早い（累積和）
coords = {"A": 0, ~~~}
ans = abs(coords[p] - cooeds[q])
----------------------------------------------------
"""

def main():
    # A -3- B -1- C -4- D -1- E -5- F -9- G
    p, q = input().split()
    points = "ABCDEFG"
    distances = [3, 1, 4, 1, 5, 9]
    
    """if points.index(p) < points.index(q):
        ans = sum(distances[points.index(p): points.index(q)])
    else:
        ans = sum(distances[points.index(q): points.index(p)])
    print(ans)"""

    idx1 = points.index(p)
    idx2 = points.index(q)
    if idx1 > idx2:
        idx1, idx2 = idx2, idx1
    ans = sum(distances[idx1:idx2])
    print(ans)

if __name__ == "__main__":
    main()