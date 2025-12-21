"""
問題URL: https://atcoder.jp/contests/abc314/tasks/abc314_b
----------------------------------------------------
結果
・

なぜ解けなかった？
・

解法ポイント、学び
・
----------------------------------------------------
"""
import sys

# これはおまじない（高速化）
input = sys.stdin.readline

def main():
    # 1. 入力受け取り
    N = int(input())
    C = []
    A = []
    for _ in range(N):
        c_val = int(input())
        # setにしておくと検索が速い
        a_set = set(map(int, input().split()))
        C.append(c_val)
        A.append(a_set)
        
    X = int(input()) # 当たり目

    # ----------------------------------------
    # 手順1：とりあえず「当たった人」を全員リストアップする
    # ----------------------------------------
    hit_people = [] # (その人の賭けた枚数, その人の番号) のペアを入れる
    
    for i in range(N):
        # X がその人の賭けた目の中にあれば「当たり」
        if X in A[i]:
            # (枚数, 番号) の順で入れると、後で扱いやすい
            hit_people.append((C[i], i + 1))
            
    # もし誰も当たってなかったら、0を出力して終わり
    if len(hit_people) == 0:
        print(0)
        print() # 空行（Pythonのprintはデフォルトで改行されるので、空文字を出力するイメージ）
        return

    # ----------------------------------------
    # 手順2：「当たった人」の中で、賭けた枚数の「最小値」を見つける
    # ----------------------------------------
    # hit_people = [(5枚, 1さん), (2枚, 2さん), (2枚, 3さん)] みたいな状態
    
    # 最小の枚数を探す
    min_count = 100 # あり得ないくらい大きい数字で初期化しておく
    for count, player_id in hit_people:
        if count < min_count:
            min_count = count
            
    # ----------------------------------------
    # 手順3：最小枚数の人だけを選んで出力する
    # ----------------------------------------
    winners = []
    for count, player_id in hit_people:
        if count == min_count:
            winners.append(player_id)
            
    # 昇順（小さい順）に並べて出力
    winners.sort()
    
    print(len(winners))
    print(*winners)

if __name__ == "__main__":
    main()