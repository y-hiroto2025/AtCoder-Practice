"""
問題URL: https://atcoder.jp/contests/abc465/tasks/abc465_b
----------------------------------------------------
----------------------------------------------------
"""
def main():
    X, Y, L, R, A, B = map(int, input().split())

    ans = 0

    for h in range(A, B):
        if L<=h and h<=R-1:
            ans += X
        else:
            ans += Y

    print(ans)

if __name__ == "__main__":
    main()