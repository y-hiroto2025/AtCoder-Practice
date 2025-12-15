"""
問題URL: https://atcoder.jp/contests/abc310/tasks/abc310_b
----------------------------------------------------
結果
・ギブアップ

なぜ解けなかった？
・

解法ポイント、学び
・
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    """
    N個商品i番目はP[i]円でc[i]個の機能を持つ
    i番目商品のj番目昨日はf[i][j]
    i番目とj番目商品で次の条件を満たすかどうか
    - p[i] >= p[j]
    - j番目はi番目の昨日をすべてもつ
    - p[i] > p[j]であるか、j番目はi番目にない機能を一つ以上持つ
    """
    N, M = map(int, input().split()) # 総数、Fの最大
    prices = []
    num_funcs = []
    funcs = []

    for _ in range(N):
        p_c_f = list(map(int, input().split()))
        prices.append(p_c_f[0])
        num_funcs.append(p_c_f[1])
        funcs.append(p_c_f[2:])

    ans = "No"
    for i in range(N):
        for j in range(N):
            if (i != j) and (prices[i] >= prices[j]) :
                print(prices[i], prices[j])
                for func in funcs[i]:
                    if not func in funcs [j]:
                        break
            



if __name__ == "__main__":
    main()