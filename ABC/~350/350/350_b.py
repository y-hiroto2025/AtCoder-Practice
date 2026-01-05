"""
問題URL: https://atcoder.jp/contests/abc350/tasks/abc350_b
----------------------------------------------------
結果
・自力（7min）

解法ポイント、学び
・^(XOR): 同じなら0、違うなら1
----------------------------------------------------
"""
def main():
    N, Q = map(int, input().split())
    T = list(map(int, input().split()))
    tooth = [1] * N

    for i in range(Q):
        """if tooth[T[i] - 1] == 1:
            tooth[T[i] - 1] = 0
        else:
            tooth[T[i] - 1] = 1"""
        tooth[T[i] - 1] ^= 1
    print(sum(tooth))

if __name__ == "__main__":
    main()