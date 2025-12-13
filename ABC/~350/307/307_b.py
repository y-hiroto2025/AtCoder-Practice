"""
問題URL: https://atcoder.jp/contests/abc307/tasks/abc307_b
----------------------------------------------------
結果
・ギブアップ

なぜ解けなかった？
・判定する組み合わせのパターンが足りていなかった。
・exit()の入れ方が良くなかった

解法ポイント、学び
・exit()=>その瞬間にプログラムを強制終了する命令なので、条件文でのbreakやreturnを使う
・文字列の結合する順番も変えないといけないので、すべての組み合わせを見る必要がある
----------------------------------------------------
"""

def main():
    num = int(input())
    S = []
    for _ in range(num):
        S.append(input())
    
    for i in range(num):
        for j in range(num):
            if i == j:
                continue
            if S[i] + S[j] == (S[i] + S[j])[::-1]:
                print("Yes")
                # exit()
                return
                
    print("No")

if __name__ == "__main__":
    main()