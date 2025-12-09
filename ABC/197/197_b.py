"""
問題URL: https://atcoder.jp/contests/abc197/tasks/abc197_b
----------------------------------------------------
結果
・ギブアップ

なぜ解けなかった？
・グリッド探索の解法を知らなかった

解法ポイント、学び
・グリッド探索

----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]

    # 現在の座標
    current_x = X - 1
    current_y = Y - 1

    ans = 1 # 自分も含めるので1

    # 上下左右の移動量リスト
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 4方向を順番に試す
    for dx, dy in dxy:
        # 現在地からスタート
        x, y = current_x, current_y
        
        while True:
            # １歩進める
            x += dx
            y += dy

            # 外に出たらストップ
            if not (0 <= x < H and 0 <= y < W):
                break

            # 壁にぶつかったらストップ
            if S[x][y] == "#":
                break

            # 範囲内で、壁でないなら見える
            ans += 1
        """
        while 0 <= x < H and 0 <= y < W and S[x][y] != "#"と書くとシンプル
        """

        print(ans)


if __name__ == "__main__":
    main()