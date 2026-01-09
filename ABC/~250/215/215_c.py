"""
問題URL: https://atcoder.jp/contests/abc215/tasks/abc215_c
----------------------------------------------------
結果
・ギブアップ
----------------------------------------------------
"""
import itertools

def main():
    S, K = input().split()
    
    # Sの並び替え全パターン(タプルのリスト)
    perms = itertools.permutations(S)
    
    # 重複を消して辞書順にならべる
    unique_perms = sorted(list(set("".join(p) for p in perms)))

    print(unique_perms[K - 1])

if __name__ == "__main__":
    main()