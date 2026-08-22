"""
問題URL: https://atcoder.jp/contests/abc052/tasks/abc052_b
----------------------------------------------------
結果
・1min
----------------------------------------------------
"""
def main():
    N = int(input())
    S = input().strip()

    x = 0
    ans = 0

    for i in range(N):
        if S[i] == "I":
            x += 1
        else:
            x -= 1

        ans = max(ans, x)

    print(ans)


if __name__ == "__main__":
    main()