"""
問題URL: https://atcoder.jp/contests/abc158/tasks/abc158_c
----------------------------------------------------
結果
・5min
----------------------------------------------------
"""
def main():
    A, B = map(int, input().split())

    for x in range(1001):
        if int(x*8/100)==A and int(x*10/100)==B:
            print(x)
            return

    print(-1)


if __name__ == "__main__":
    main()