"""
問題URL: https://atcoder.jp/contests/abc326/tasks/abc326_b
----------------------------------------------------
結果
・自力（7min）
----------------------------------------------------
"""
def main():
    N = int(input())

    for i in range(N, 920):
        n = int(str(i)[0]) * int(str(i)[1])

        if n == int(str(i)[2]):
            print(i)
            break

if __name__ == "__main__":
    main()