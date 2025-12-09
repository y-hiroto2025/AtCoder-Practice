"""
問題URL: https://atcoder.jp/contests/abc337/tasks/abc337_b
----------------------------------------------------
結果
・自力（15min）

解法ポイント、学び
・特定の文字の出現カウントはcountメソッドを使う
・文字列もソートができる
----------------------------------------------------
"""

def main():
    S = input()
    A_count = S.count("A")
    B_count = S.count("B")
    C_count = S.count("C")
    ABC = "A" * A_count + "B" * B_count + "C" * C_count

    if S == ABC:
        print("Yes")
    else:
        print("No")

"""
「文字列がソートされているかどうか？」と解釈できる
~
sorted_S = "".join(sorted(S))
if S == sorted_S:
~
"""

if __name__ == "__main__":
    main()