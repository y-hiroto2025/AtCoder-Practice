"""
問題URL: https://atcoder.jp/contests/abc319/tasks/abc319_b
----------------------------------------------------
結果
・ギブアップ

なぜ解けなかった？
・for x in range(1, 10)をfor x in range(1, 9)としていた
----------------------------------------------------
"""
def main():
    N = int(input())
    ans = []
    divisor = []
    for x in range(1, 10):
        if N % x == 0:
            divisor.append(x)
 
    for i in range(N + 1):
        exist_j = False

        for j in divisor:
            if i % (N//j) == 0:
                ans.append(str(j))
                exist_j = True
                break
        if not exist_j:
            ans.append("-")

    print("".join(ans))

if __name__ == "__main__":
    main()