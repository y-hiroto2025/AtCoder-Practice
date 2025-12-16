"""
問題URL: https://atcoder.jp/contests/abc311/tasks/abc311_b
----------------------------------------------------
結果
・ギブアップ

なぜ解けなかった？
・リストを縦に見ていく発想がなかった
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, D = map(int, input().split())
    S = [input().strip() for _ in range(N)]
    
    ans = 0
    current_ren = 0

    # 1~D日目まで縦に見ていく
    for day in range(D):
        everyone_free = True # その日、全員暇？
        for person in range(N):
            if S[person][day] == "x": # 誰か一人でもxならダメ
                everyone_free = False
                break
        if everyone_free:
            current_ren += 1
            ans = max(ans, current_ren) # 最高記録を更新
        else:
            current_ren = 0 # 誰かがxなら連続記録が途切れる
    print(ans)
        
"""
all()を使うとシンプルになる
for day in range(D):
    if all(S[i][day] == "o" for i in range(N)):
        current_ren += 1
        ans = max(ans, current_ren)
    else:
        current_ren = 0
"""


if __name__ == "__main__":
    main()