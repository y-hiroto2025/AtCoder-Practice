"""
問題URL: https://atcoder.jp/contests/abc131/tasks/abc131_b
----------------------------------------------------
結果
・ギブアップ

なぜ解けなかった？
・2番目の条件が間違っていた。0が含まれないけど正負が混ざっている状況に対応できない。

解法ポイント、学び
・制約が緩いときは場合分けよりも全データをリストにいれてから探す方が良い
・0に近い=> 絶対値が最小
・min(list, key=abs)にすると、絶対値の小さい順で探してくれる
----------------------------------------------------
"""

def main():
    N, L = map(int, input().split())

    apples = [L + i for i in range(N)] # ループの最初を0にすれば-1を書かなくても良い
    eat_apple = min(apples, key=abs) # key=abs: 絶対値が小さい順で最小値を探す
    ans = sum(apples) - eat_apple

    """ans = 0

    if L + N < 0:
        for i in range(1, N):
            ans += L + i - 1
    else:
        if L < 0:
            for i in range(1, N + 1):
                ans += L + i - 1
        else:
            for i in range(2, N + 1):
                ans += L + i - 1"""
    
    print(ans)

if __name__ == "__main__":
    main()