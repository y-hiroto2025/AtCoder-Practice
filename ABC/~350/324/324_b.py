"""
問題URL: https://atcoder.jp/contests/abc324/tasks/abc324_b
----------------------------------------------------
解法ポイント、学び
・掛け算で構成を作るのがムズイときは割り算で考えてみると簡単になることがある
----------------------------------------------------
"""
def main():
    N = int(input())

    while N % 2 == 0:
        N = N // 2
    while N % 3 == 0:
        N = N // 3
    
    if N == 1:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()