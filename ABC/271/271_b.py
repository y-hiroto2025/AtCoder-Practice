"""
問題URL: https://atcoder.jp/contests/abc271/tasks/abc271_b
----------------------------------------------------
結果
・自力（15mim）

解法ポイント、学び
・スライスは無駄がある
----------------------------------------------------
"""
import sys

# これで入力を高速化できる
input = sys.stdin.readline

def main():
    N, Q = map(int, input().split()) # N個の数列、Q個のクエリ
    a = []
    
    for _ in range(N):
        n = list(map(int, input().split()))
        # a.append(n[1:]) スライスはpython内部でリストのコピーが作られるので無駄が多い
        a.append(n) # そのまま保存しておく

    for _ in range(Q):
        s_k, t_k = map(int, input().split())
        # print(a[s_k - 1][t_k - 1])
        print(a[s_k - 1][t_k])

if __name__ == "__main__":
    main()