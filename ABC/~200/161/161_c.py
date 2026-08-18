"""
問題URL: https://atcoder.jp/contests/abc161/tasks/abc161_c
----------------------------------------------------
----------------------------------------------------
"""
def main():
    N, K = map(int, input().split())

    print(min(N%K, K - N%K))


if __name__ == "__main__":
    main()