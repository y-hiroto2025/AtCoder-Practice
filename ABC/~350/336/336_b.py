"""
問題URL: https://atcoder.jp/contests/abc336/tasks/abc336_b
----------------------------------------------------
結果
・自力（5min）

解法ポイント、学び
・
----------------------------------------------------
"""
def main():
    N = int(input())
    """N_binary = bin(N)[2:]"""
    ctz = 0

    """for i in range(len(N_binary)):
        if N_binary[-i - 1] != "1":
            ctz += 1
        else:
            break"""
    while N % 2 == 0:
        N //= 2
        ctz += 1

    print(ctz)

if __name__ == "__main__":
    main()