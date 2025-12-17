"""
問題URL: https://atcoder.jp/contests/abc427/tasks/abc427_b
----------------------------------------------------
結果
・自力（30min）

解法ポイント、学び
・mapを使うことで、forループを回さなくても各桁の和を求められる
----------------------------------------------------
"""

def main():
    N = int(input())
    current_sum = 1 # リストで管理する必要はない

    for _ in range(N - 1):
        s_val = str(current_sum)
        x = sum(map(int, s_val))
        
        current_sum += x
    print(current_sum)

if __name__ == "__main__":
    main()