"""
問題URL: https://atcoder.jp/contests/abc321/tasks/abc321_b
----------------------------------------------------
結果
・ギブアップ

なぜ解けなかった？
・複雑な条件文で解こうとして、わからなくなってしまった

解法ポイント、学び
・制約が緩いので全探索でやるほうが単純になる
----------------------------------------------------
"""
def main():
    # Nラウンドで得た各得点のうち最小最大を抜いた数の和がXを超えないといけない
    N, X = map(int, input().split())
    A = list(map(int, input().split())) # N-1までのスコア

    for score in range(101):
        current_score = A + [score]

        final_score = sum(current_score) - max(current_score) - min(current_score)

        if final_score >= X:
            print(score)
            return
    
    print(-1)

if __name__ == "__main__":
    main()