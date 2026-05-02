"""
問題URL: https://atcoder.jp/contests/abc421/tasks/abc421_b
----------------------------------------------------
結果
・自力（6min）
----------------------------------------------------
"""
def main():
    X, Y = map(int, input().split())

    a = [X, Y]

    for i in range(1, 9):
        a.append(int(str(a[i] + a[i-1])[::-1]))
    
    print(a[-1])


if __name__ == "__main__":
    main()