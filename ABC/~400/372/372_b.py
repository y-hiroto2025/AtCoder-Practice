"""
問題URL: https://atcoder.jp/contests/abc372/tasks/abc372_b
----------------------------------------------------
結果
・自力（10min）
----------------------------------------------------
"""
def main():
    M = int(input())

    ans = []
    for i in range(11):
        ans += [i] * (M % 3)
        M //= 3
    print(len(ans))
    print(*ans)

if __name__ == "__main__":
    main()