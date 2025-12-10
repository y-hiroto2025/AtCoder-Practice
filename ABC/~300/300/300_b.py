"""
問題URL: https://atcoder.jp/contests/abc300/tasks/abc300_b
----------------------------------------------------
結果
・ギブアップ

なぜ解けなかった？
・制約を見落としており、全探索でいいことに気づかなかった
・

解法ポイント、学び
・制約が小さいならまずは全探索を疑う
・端と端がつながっているなら % を使う
・2次元配列のコピーはcopyモジュールか内包表記を使わないとおかしくなる
----------------------------------------------------
"""

def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    B = [input() for _ in range(H)]
    # 1. 縦にずらす量 s
    for s in range(H):
        # 2. 横にずらす量 t
        for t in range(H):

            # (s,t)でA,Bが一致するか全マス確認
            is_match = True # フラグ(flag)

            for i in range(H):
                for j in range(W):
                    # 移動後の座標を計算して確かめる
                    # %を使うことで、端を超えたら自動的に0に戻る
                    if A[(i + s) % H][(j + t) % W] != B[i][j]:
                        is_match = False
                        break
                if not is_match:
                    break
            
            if is_match:
                print("Yes")
                return
    print("No")

if __name__ == "__main__":
    main()