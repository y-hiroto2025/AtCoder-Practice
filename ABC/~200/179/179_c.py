"""
問題URL: https://atcoder.jp/contests/abc179/tasks/abc179_c
----------------------------------------------------
----------------------------------------------------
"""
def main():
    N = int(input())

    ans = 0
    for a in range(1, N + 1):
        ans += (N - 1) // a

    print(ans)

if __name__ == "__main__":
    main()